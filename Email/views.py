from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

import time

def sending_mail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_email = request.POST.get('recipient_email')
        from_email = settings.DEFAULT_FROM_EMAIL
        num_emails = int(request.POST.get('num_emails'))
        time_gap = int(request.POST.get('time_gap'))

        for _ in range(num_emails):
            send_mail(subject, message, from_email, [recipient_email])
            print("Email sent")
            
            if time_gap > 0:
                time.sleep(time_gap)  # Pause for the specified time gap

        messages.success(request, f'{num_emails} email(s) sent successfully with a {time_gap} second(s) gap!')
        
        return redirect('sending_mail')
    
    return render(request, 'mail.html')
