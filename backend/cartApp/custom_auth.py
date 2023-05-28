from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomAuth(JWTAuthentication):
    def authenticate(self, request):
        result = super(CustomAuth, self).authenticate(request)
        if result:
            user, token = result
            return user, token
        return None, None