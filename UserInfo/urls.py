from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/register', views.Index, name='register'),
    path('register/register_user', views.register_user, name='register_user'),
    path('register/updated_user', views.update_profile, name='update_profile'),
    path('user/dashboard', views.Dashboard, name='dashboard'),
]