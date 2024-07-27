from django.shortcuts import render, redirect
from django.views.generic.base import View
from . import forms
from .models import User
from django.contrib.auth import authenticate, login


class SignupView(View):
  def get(self, request):
    signupform = forms.SignupForm()
    return render(request, 'authentication/signup.html', context={
      'signupform' : signupform,
    })
    
  def post(self, request):
    signupform = forms.SignupForm(request.POST)
    if signupform.is_valid():
      signupform.save()
      return redirect('bookshelf:login')
    return render(request, 'authentication/signup.html', context={
      'signupform' : signupform,
    })


class LoginView(View):
  def get(self, request):
    loginform  = forms.LoginForm()
    return render(request, 'authentication/login.html', context={
      'loginform' : loginform,
    })
    
  def post(self, request):
    loginform = forms.LoginForm(request.POST)
    if loginform.is_valid():
      email = loginform.cleaned_data['email']
      password = loginform.cleaned_data['password']
      user = authenticate(username=email, password=password)
      
      if user is not None:
        login(request, user)
        return redirect('bookshelf:signup')
      
      else:
        loginform.add_error(None, 'メールアドレスまたはパスワードが違います。')
    
    return render(request, 'authentication/login.html', context={'loginform':loginform})