from django import forms
from django.contrib.auth import get_user_model
from .models import User
import re
from django.core.exceptions import ValidationError


User = get_user_model()

class SignupForm(forms.ModelForm):
  confirm_password = forms.CharField(label='パスワード再入力')
  
  class Meta:
    model = User
    fields = ('name', 'email', 'password')
    labels = {'name':'ユーザー名', 'email':'メールアドレス','password':'パスワード'}
   
  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      confirm_password = cleaned_data.get('confirm_password')
      if password != confirm_password:
        self.add_error('confirm_password', 'パスワードが一致しません。')
      return cleaned_data
      
  def clean_password(self):
    password = self.cleaned_data.get('password')
    if password:
      if len(password) < 10:
        self.add_error('password','10文字以上で入力してください。')
      
      if not re.match('(?=.*\d)(?=.*[a-z])[a-zA-Z\d]{10,}', password):
        self.add_error('password', 'パスワードは半角英数で入力してください。')
    return password

  def save(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    user = User(name=name, email=email)
    user.set_password(self.cleaned_data['password'])
    user.save()
    
class LoginForm(forms.Form):
  email = forms.EmailField(max_length=254)
  password = forms.CharField(max_length=64)
  
  def clean_password(self):
    password = self.cleaned_data.get('password')
    if password:
      if len(password) < 10:
        self.add_error('password', '10文字以上で入力してください。')
      
      if not re.match('\A(?=.*?[a-z])(?=.*?\d)[a-z\d]{10,128}\Z(?i)', password):
        raise ValidationError('パスワードは半角英数で入力してください。')
    return password
