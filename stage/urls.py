from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'task-home'),
    path('about/', views.about, name = 'task-about'),

]