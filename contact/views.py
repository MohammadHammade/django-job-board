from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .models import info
# Create your views here.


def send_message(request):
    myinfo = info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        #subject
        #message
        #from
        #to
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
    return render(request,'contact/contact.html',{'myinfo':myinfo})