from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, SignupForm

User = get_user_model()

class CustomizeUsreAdmin(UserAdmin):
  form = UserChangeForm #ユーザー編集画面で使うフォーム
  add_form = SignupForm
  
  list_display = ('name', 'email') #一覧画面で表示する要素の定義
  ordering = ('name',)
  
  #一覧画面に表示する
  fieldsets = (
    ('ユーザー情報', {'fields':('name', 'email', 'password')}),
    ('パーミッション', {'fields':('is_staff', 'is_active', 'is_superuser')}),
  )
  
  add_fieldsets = (
    ('ユーザー情報',{
      'fields' : ('name', 'email', 'password', 'confirm_password')
      }),
  )
  
admin.site.register(User, CustomizeUsreAdmin)