from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.register_customer_view),
    path('users/<int:user_id>/', views.user_detail),
]
