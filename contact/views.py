from django.shortcuts import render
from django.core.mail import send_mail
from .models import Info
from django.conf import settings

# Create your views here.

def send_message(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    myinfo = Info.objects.last()
    return render (request, 'contact/contact.html', {'myinfo' : myinfo})
