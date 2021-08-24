from django.contrib.auth import views
from django.urls import path
from credentialapp import views


urlpatterns = [
    path('', views.register),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]
