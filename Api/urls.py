from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<int:pk>/', views.taskDetail, name='task-detail'),
]
