from django.shortcuts import render, redirect
from django.views.generic.base import View
from . import forms
from django.contrib.auth import authenticate, login


class SignupView(View):
  def get(self, request):
    signup_form = forms.SignupForm()
    return render(request, 'authentication/signup.html', context={
      'signup_form' : signup_form,
    })
    
  def post(self, request):
    signup_form = forms.SignupForm(request.POST)
    if signup_form.is_valid():
      signup_form.save()
      #TODO：ホーム画面を作ったら、そっちに遷移させるようリダイレクト先変更
      return redirect('bookshelf:login')
    return render(request, 'authentication/signup.html', context={
      'signup_form' : signup_form,
    })


class LoginView(View):
  def get(self, request):
    login_form  = forms.LoginForm()
    return render(request, 'authentication/login.html', context={
      'login_form' : login_form,
    })
    
  def post(self, request):
    login_form = forms.LoginForm(request.POST)
    if login_form.is_valid():
      email = login_form.cleaned_data['email']
      password = login_form.cleaned_data['password']
      user = authenticate(username=email, password=password)
      
      if user is not None:
        login(request, user)
        #TODO：ホーム画面を作ったら、そっちに遷移させるようリダイレクト先変更
        return redirect('bookshelf:signup')
      
      else:
        login_form.add_error(None, 'メールアドレスまたはパスワードが違います。')
    
    return render(request, 'authentication/login.html', context={'login_form':login_form})
