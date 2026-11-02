from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("register/<str:usertype>/", views.registerpage, name="register"),
]