from django.shortcuts import render, redirect
from django.views.generic.base import (
  View, 
)
from . import forms
from .models import User



class SignupView(View):
  def get(self, request, *args, **kwargs):
    signupform = forms.SignupForm()
    return render(request, 'signup.html', context={
      'signupform' : signupform,
    })
    
  def post(self, request, *args, **kwargs):
    signupform = forms.SignupForm(request.POST)
    if signupform.is_valid():
      signupform.save()
      return redirect('bookshelf:login')
    return render(request, 'signup.html', context={
      'signupform' : signupform,
    })


class LoginView(View):
  def get(self, request, *args, **kwargs):
    loginform  = forms.LoginForm()
    return render(request, 'login.html', context={
      'loginform' : loginform,
    })
    
  def post(self, request, *args, **kwargs):
    loginform = forms.LoginForm(request.POST)
    if loginform.is_valid():
      loginform.save()
      return redirect('bookshelf:signup')
    return render(request, 'login.html', context={
      'loginform' : loginform,
    })