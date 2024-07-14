from django.urls import path
from .views import SignupView, LoginView





app_name = 'BookshelfApp'
urlpatterns = [
  path('signup/',SignupView.as_view(), name='signup'),
  path('login/',LoginView.as_view(), name='login'),
]