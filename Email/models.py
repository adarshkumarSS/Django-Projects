from django.db import models
from Email.models import *
# Create your models here.
class mail(models.Model):
    sender_email =  models.EmailField()
    subject = models.TextField()
    message = models.TextField()