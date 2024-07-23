from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def sendmail(request):
    current_user = request.user
    if current_user.is_superuser:
        if request.method=='POST':
            message = request.POST['message']
            email = request.POST['email']
            send_mail(
                'System Email',
                message,
                'settings.EMAIL_HOST_USER', #kim gönderecek
                [email], #kime gönderilecek
                fail_silently=False
            )
        return render(request,'mail.html')
    else:
        messages.error(request,'Yalnızca yöneticiler bu işlemi yapabilir!')
        return redirect('login')
   