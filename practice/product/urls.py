from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('list/', views.list),
    path('detail/<int:pk>', views.detail),
    path('delete/<int:pk>', views.delete)


]
