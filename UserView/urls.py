from django.urls import path
from . import views

urlpatterns = [
    path('', views.pre_home_page, name='prehome'),
    path('home/', views.home_page, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('update_dryer/<int:pk>/', views.update_dryer, name='update-dryer'),
    path('update_laundry/<int:pk>/', views.update_laundry, name='update-laundry')
]