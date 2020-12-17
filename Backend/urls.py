from django.urls import path
from . import views

urlpatterns = [
    path("backend/", views.adminDashboard, name='backend'),
    path("backend/idea/list", views.Idea, name='admin_idea'),
    path("updateIdea", views.updateIdea, name='updateIdea'),
    path("backend/idea/idea_edit/<int:id>", views.IdeaEdit, name='edit_idea'),
    path("dreamer/idea/image/<int:id>", views.IdeaImages),
    path("backend/dreamer/idea/image/delete/<int:id>", views.DeleteIdeaImages),

    path("backend/user/list", views.GetUser, name="admin_user"),
    path("backend/user/user_edit/<int:id>", views.UserEdit, name='edit_user'),
    path("backend/updateUser", views.updateUser, name='updateUser'),
]