from .models import student
import time
from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "This email is from Django Server"
    message = "This email is a test message from Django Server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['mithles2k50@gmail.com']

    return send_mail(subject , message , from_email , recipient_list)