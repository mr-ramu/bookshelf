from django.db import models
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser, PermissionsMixin,
)

class UserManager(BaseUserManager):
  def create_user(self,name, email, password):
    user = self.model(
      username = name,
      email = email,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, name, email, password):
    user = self.model(
     name = name,
     email = self.normalize_email(email),
    )
    user.set_password(password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser,PermissionsMixin):
  name = models.CharField(max_length=10)
  email = models.EmailField(max_length=254, unique=True)
  password = models.CharField(max_length=128) 
  icon = models.CharField(max_length=500, null=True, blank=True, default='static/images/default_user_icon.png') 
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']
  objects = UserManager()
  
  def __str__(self):
    return self.email