from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('signup', views.signup_page, name='signup'),
    path('login', views.login_page, name='login')
]