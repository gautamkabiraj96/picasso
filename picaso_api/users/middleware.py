from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse
from users.models import AccessTokenBlacklist
from rest_framework.authtoken.models import Token

class JWTBlacklistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token_str = auth_header.split(" ")[1]

            try:
                token = AccessToken(token_str)

                if AccessTokenBlacklist.objects.filter(token=token_str).exists():
                    return JsonResponse({"error": "Token has been revoked. Please log in again."}, status=401)

                return None

            except Exception as e:
                return JsonResponse({"error": "Invalid token"}, status=401)

class TokenUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for the Authorization header
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            # Extract token key
            token_key = auth_header.split(' ')[1]
            
            try:
                # Get the token and user
                token = Token.objects.get(key=token_key)
                # Attach the user to the request
                request.user = token.user
            except Exception as e:
                # Token not found, don't attach user
                pass
                
        return self.get_response(request)