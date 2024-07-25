from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client
from vege.seed import *



def send_email(request):
    send_email_to_client()
    return redirect('/')








def home(request):
    peoples=[
        {'name':'adarsh','age':12},
        {'name':'mithles','age':18},
        {'name':'chaitanya','age':3},
        {'name':'surya','age':63}
    ]
   
    vegetables={'pumpkin','tomato','potato'}
    return render(request,"home\index.html", context={'page':'Django Server','peoples':peoples,'veetables':vegetables})
def about(request):
    context = {'page' : 'about'}
    return render(request,"home/about.html", context)
def contact(request):
    context = {'page' : 'contact'}
    return render(request,"home/contact.html", context)
