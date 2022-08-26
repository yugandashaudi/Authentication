from atexit import register
from pickle import TRUE
from  rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import *
from .emails import send_email_with_otp
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




User = get_user_model()



class RegisterEmail(APIView):
    def post(self,request):
        serializer = RegisterEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       

        return Response('The email has been registered')




class UserRegisteration(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password1 = serializer.validated_data.get('password')
        password2 = serializer.validated_data.get('password2')
        if password1 != password2:
            return Response('Two password doesnot match')
        serializer.save()

        return Response({'msg':'The sign up has been done sucessfully'},status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            tokens = get_tokens_for_user(user)
            return Response({'msg':'The user has been sucessfully logged in','tokens':tokens,},status=status.HTTP_200_OK)

        return Response('Email or password is incorrect')
        
        