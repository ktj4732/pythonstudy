from django.urls import path
from . import views

urlpatterns = [

    path('product/<int:pk>/', views.orderPage),
    path('list/', views.orderList),
    path('delete/<int:pk>', views.delete),
    path('detail/<int:pk>', views.detail),
    path('update/<int:pk>', views.update)

]
