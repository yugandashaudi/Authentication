from rest_framework import serializers 
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterEmailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        
        fields=['email']

    def create(self,validated_data):
        email = validated_data.get('email')
        user = User.objects.create(email=email)
        user.is_active=False
        user.save()
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(max_length=100)
    email_address = serializers.CharField(max_length=100)
    class Meta:
        model =User
        fields=['email_address','username','password','password2']

    def validate(self,arrgs):
        email = arrgs.get('email_address')
        user_email = User.objects.filter(email = email).first()

        if user_email is None:
            raise serializers.ValidationError('The email is not verified through otp')

   

    def create(self,validate_data):
        validate_data.pop('password2')
        email = validate_data.pop('email_address')
        user_email = User.objects.filter(email = email).first()
        user_email.username=validate_data.get('username')
        user_email.set_password(validate_data.get('password'))   
        user_email.is_active = True
        user_email.save()
        return user_email
        



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100,write_only=True)
    class Meta():
        fields=['email','password']