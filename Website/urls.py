from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('idea/list', views.idea_list, name='idea_list'),
    path('idea/details/<int:id>', views.idea_details, name='idea_details'),
    path('idea/list/<int:id>', views.SearchIdea, name='search_idea'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('faqs', views.faqs, name='faqs'),
    path('all_locations/', views.all_locations, name='all_locations'),
    path('search/', views.search, name='search'),
    path('search_idea/', views.search_idea, name='search_idea'),
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path('login', views.loginUser, name='login'),
]