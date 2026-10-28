from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_snippet),
    path('getall/',views.get_snippet),
]
