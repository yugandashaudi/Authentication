from django.urls import path 
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_email/',RegisterEmail.as_view(),name='register_email'),
    path('user_register/',UserRegisteration.as_view(),name='user_register'),
   
    path('login/',LoginUser.as_view(),name='login')

]