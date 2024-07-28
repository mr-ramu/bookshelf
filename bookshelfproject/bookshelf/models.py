from django.db import models
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser,
)

class UserManager(BaseUserManager):
  def create_user(self,name, email, password):
    user = self.model(
      username = name,
      email = email,
    )
    email = self.normalize_email(email)
    user.set_password(password)
    user.save(using=self._db)
    return user
  

class User(AbstractBaseUser):
  name = models.CharField(max_length=20)
  email = models.EmailField(max_length=254, unique=True)
  password = models.CharField(max_length=64) 
  icon = models.CharField(max_length=500,default='static/images/default_user_icon.png') 
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']
  objects = UserManager()
  
  def __str__(self):
    return self.email
