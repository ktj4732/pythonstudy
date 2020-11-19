from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list),
    path('write/', views.write),
    path('detail/<int:pk>', views.detail),
    path('delete/<int:pk>', views.delete),
    path('update/<int:pk>', views.update),

]
