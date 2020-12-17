from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dreamer/post-idea', views.PostIdea, name='post_idea'),
    path('SubmitIdea', views.SubmitIdea, name='SubmitIdea'),
    path("action/<int:id1>/<int:id2>", views.ChangeStatus, name='changeStatus'),
    path("idea/delete/<int:id>", views.IdeaDelete, name='idea_delete'),
]