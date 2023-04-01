from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path

from apps.user.views import TokenCustomView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="user_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
