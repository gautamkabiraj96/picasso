from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.authtoken.models import Token
import google.oauth2.id_token
import google.auth.transport.requests
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, GoogleAuthSerializer

User = get_user_model()

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_200_OK)

class UserView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

class GoogleLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = GoogleAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        id_token = serializer.validated_data.get('auth_token')
        
        try:
            # Verify the token with Google
            CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"  # Get this from Google Developer Console
            request_google = google.auth.transport.requests.Request()
            id_info = google.oauth2.id_token.verify_oauth2_token(id_token, request_google, CLIENT_ID)
            
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
                
            # Get user data from Google
            google_id = id_info['sub']
            email = id_info['email']
            name = id_info.get('name', '')
            profile_picture = id_info.get('picture', '')
            
            # Check if user exists in DB
            try:
                user = User.objects.get(email=email)
                # Update Google ID if not set
                if not user.google_id:
                    user.google_id = google_id
                    user.profile_picture = profile_picture
                    user.save()
            except User.DoesNotExist:
                # Create new user
                names = name.split(' ', 1)
                first_name = names[0]
                last_name = names[1] if len(names) > 1 else ''
                
                user = User.objects.create_user(
                    username=email.split('@')[0],
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    google_id=google_id,
                    profile_picture=profile_picture,
                    is_verified=True
                )
                # Set unusable password as user will login via Google
                user.set_unusable_password()
                user.save()
            
            # Generate token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
