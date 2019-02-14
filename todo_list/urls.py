from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('status_completed/<list_id>', views.delete, name="status_completed"),
    path('status_not_completed/<list_id>', views.delete, name="status_not_completed"),
]
