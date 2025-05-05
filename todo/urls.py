from django.urls import path
from .views import todo_list_create, delete_task, edit_task, api_todo_list, signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', todo_list_create, name='todo_list_create'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('api/todos/', api_todo_list, name='api_todo_list'),
]
