from django.shortcuts import redirect, render
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .tokens import account_activation_token

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None: 
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.info(request,'Disabled Account')
            else:
                messages.info(request,'Check your Username and Password')
    else:
        form = LoginForm()
    
    return render(request,'login.html',{'form':form,})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate your account'
            email_body = ''
            message = render_to_string('acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })            
            to_email = form.cleaned_data.get('email')
            email=EmailMessage(
                email_subject,message,to=[to_email]
            )
            email.send()
            msg = 'Please confirm your email address to complete'
            img_url = "{% static 'images/time-left.png' %}"
            context = {
                'msg': msg,
                'img_url': img_url,
            }
            return render(request,'Email.html',context)
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form,})

def activate(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request,'Email.html',{'msg':'Thank you for your email confirmation. Now you can login!','img_url':'verified.png'})
    else:
        return render(request,'Email.html',{'msg':'Activation link is invalid!'})
    

def user_logout(request):
    logout(request)
    return redirect('index')