from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from accounts.models import *
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from accounts.forms import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def login_view(request):
    #if request.user.is_authenticated:
     #   msg = f'You are already logged in as {request.user.username}'
    #else:
     #   msg = 'You are not  logged in'
    #return render(request, 'accounts/login.html', {'msg': msg})
    
    
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.add_message(request,messages.SUCCESS,'Login was successful')
                return redirect('/')
            else:
                 messages.add_message(request,messages.ERROR,'The desired person was not found')
        form = LoginForm()         
        return render(request, "accounts/login.html", {'form':form})
    else:
          return redirect('/')
        





def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def logout_view(request):
    #  if request.user.is_authenticated:
          logout(request)
          return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
              form=SignUpForm(request.POST)
              if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Now you can sign in')
                return redirect('accounts:login')
             
              else:
                messages.add_message(request, messages.ERROR, 'something went wrong')
        # form=UserCreationForm()
        form=SignUpForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
          return redirect('/')
   
   
class ChangePasswordView(PasswordChangeView):
     template_name = 'accounts/change_password.html'
     success_url = reverse_lazy('accounts:login')
     form_class = ChangePasswordForm 
    
class PasswordReset(PasswordResetView):
    template_name="accounts/password_reset_form.html"
    success_url=reverse_lazy("accounts:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="accounts/password_reset_done.html"
    success_url=reverse_lazy("accounts:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="accounts/password_reset_confirm.html"
    success_url=reverse_lazy("accounts:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="accounts/password_reset_complete.html"
    

