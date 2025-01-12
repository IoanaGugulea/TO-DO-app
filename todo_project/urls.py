from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.task_list, name='task_list'),  # Home page, only for logged-in users
    path('add/', views.add_task, name='add_task'),  # Page to add a new task
    path('update/<int:task_id>/', views.update_task, name='update_task'),  # Update task page
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task page

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('accounts/register/', views.register, name='register'),  # Registration page
    path('update/<int:task_id>/', views.update_task, name='update_task'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

