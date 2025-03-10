from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse
from users.models import AccessTokenBlacklist 

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
