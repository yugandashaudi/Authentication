from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


def send_email_with_otp(email):
    subject = 'Your Verification Email'
    otp = random.randint(10000,99999)
    message = f'Your OPT Verificatiion code is {otp}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,[email])
    user = User.objects.filter(email=email).first()
    user.otp=otp
    user.save()