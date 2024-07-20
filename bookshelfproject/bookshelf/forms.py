from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import User
import re
from django.contrib.auth import authenticate


User = get_user_model()

class SignupForm(forms.ModelForm):
  confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput)
  
  class Meta:
    model = User
    fields = ('name', 'email', 'password')
    labels = {'name':'ユーザー名', 'email':'メールアドレス','password':'パスワード'}
    widgets = {'password':forms.PasswordInput}
   
  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      confirm_password = cleaned_data.get('confirm_password')
      if password != confirm_password:
        raise ValidationError('パスワードが一致しません。')
      return cleaned_data
      
  def clean_password(self):
    password = self.cleaned_data.get('password')

    if password:
      if len(password) < 10:
        raise ValidationError('10文字以上で入力してください。')
      
      if not re.match('^[0-9a-zA-Z]*$', password):
        raise ValidationError('パスワードは半角英数で入力してください。')

    return password  


  def save(self, commit=True):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    
    form = User(name=name, email=email)
    form = super().save(commit=False)
    form.set_password(self.cleaned_data['password'])
    if commit:
      form.save()
    
    

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('email', 'password')
    labels = {'email':'メールアドレス','password':'パスワード'}
    widgets = {'password':forms.PasswordInput}
    
  def clean(self):
      cleaned_data = super().clean()
      email = cleaned_data.get('email')
      password = cleaned_data.get('password')
      
      if email and password:
        user = authenticate(email=email, password=password)
        
      if not user:
        raise ValidationError('メールアドレスまたはパスワードが違います。')
      return     
