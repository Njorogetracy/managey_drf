from rest_framework.decorators import api_view
from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my managey_drf API!"
    })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response

#Added a custom login view
class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        user_serializer = self.get_serializer(self.user)
        response.data.update(user_serializer.data)
        return response