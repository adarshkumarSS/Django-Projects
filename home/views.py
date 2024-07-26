from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client, send_email_with_attachments
from vege.seed import *
from django.conf import settings
from home.models import car

#def send_email(request):
    #send_email_to_client()
    #return redirect('/')

def send_email(request):
    subject = "This email is from Django server with attachment"
    message = "this attached file is for you"
    recipient_list = ["zainadarsh@gmail.com"]
    file_path = f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachments(subject, message, recipient_list, file_path)
    return redirect('/')

def home(request):

    car.objects.create(car_name = f'{random.randint(0,100)}')

    peoples=[
        {'name':'adarsh','age':12},
        {'name':'mithles','age':18},
        {'name':'chaitanya','age':3},
        {'name':'surya','age':63}
    ]
   
    vegetables={'pumpkin','tomato','potato'}
    return render(request,"home/index.html", context={'page':'Django Server','peoples':peoples,'veetables':vegetables})
def about(request):
    context = {'page' : 'about'}
    return render(request,"home/about.html", context)
def contact(request):
    context = {'page' : 'contact'}
    return render(request,"home/contact.html", context)
