from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from .models import AccessTokenBlacklist 
import logging

logger = logging.getLogger("django")
User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "accessToken": str(refresh.access_token),
                "refreshToken": str(refresh),
            })
        
        logger.error("Invalid Credentials")
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refreshToken")
        try:
            refresh = RefreshToken(refresh_token)
            return Response({"accessToken": str(refresh.access_token)})
        except Exception:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refreshToken")
            access_token = request.headers.get("Authorization").split(" ")[1]
            
            if not refresh_token or not access_token:
                return Response({"error": "Both access and refresh token are required!"}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken(refresh_token)
            refresh.blacklist()
            
            AccessTokenBlacklist.objects.create(token=access_token)

            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": "Invalid refresh token or already blacklisted!"}, status=status.HTTP_400_BAD_REQUEST)
