from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_Data),
    path('add/', views.add_Data),
    path('delete/<str:pk>/', views.delete_Data),
    path('patch/<str:pk>/', views.partial_update_Data),
    path('put/<str:pk>/', views.update_Data)
]