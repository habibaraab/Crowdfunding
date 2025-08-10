# projects/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as project_views


urlpatterns = [
    path('', project_views.home, name='home'),
    path('projects/', project_views.project_list, name='project_list'), # <-- أضف هذا
    path('projects/create/', project_views.create_project, name='create_project'), # <-- أضف هذا
    path('register/', project_views.register, name='register'),
        path('projects/<int:project_id>/', project_views.project_detail, name='project_detail'), # <-- أضف هذا
    path('login/', auth_views.LoginView.as_view(template_name='projects/login.html'), name='login'),
     path('projects/<int:project_id>/', project_views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/edit/', project_views.edit_project, name='edit_project'), # <-- أضف هذا
    path('projects/<int:project_id>/delete/', project_views.delete_project, name='delete_project'), # <-- أضف هذا
    path('logout/', project_views.logout_view, name='logout'),

]

# projects/urls.py
# ...