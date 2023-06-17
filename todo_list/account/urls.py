from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:id>/complete/', views.task_complete, name='task_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
