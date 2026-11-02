from django.urls import path

from . import views

app_name = "student_management"

urlpatterns = [
    path('homepage',views.homepage,name='homepage'),
]