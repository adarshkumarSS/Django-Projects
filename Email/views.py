from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.http import HttpResponse

def sending_mail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_email = request.POST.get('recipient_email')
        from_email = settings.DEFAULT_FROM_EMAIL
        
        recipient_list = [recipient_email]
        
        send_mail(subject, message, from_email, recipient_list)
        print("executing mail")
        
        messages.success(request, 'Email sent successfully!')
        
        return redirect('sending_mail')
    
    return render(request, 'mail.html')
