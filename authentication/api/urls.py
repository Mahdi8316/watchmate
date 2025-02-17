from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from authentication.api.views import reg_view, logout_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', reg_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
