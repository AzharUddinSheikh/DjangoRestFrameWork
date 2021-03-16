from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name='api-overview')
]
