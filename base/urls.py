from django.urls import path
from . import views



urlpatterns = [
    path('', views.loginUser, name='login'),
    path('', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
]