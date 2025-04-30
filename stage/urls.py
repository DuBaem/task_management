from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'task-login'),
    path('signup/', views.signup, name = 'task-signup'),
]