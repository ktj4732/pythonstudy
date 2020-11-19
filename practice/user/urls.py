from django.urls import path
from . import views

# /user/*
urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('myinfo/', views.myinfo),
]
