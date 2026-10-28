from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token



from . import views

app_name = "accounts"

urlpatterns = [
    path('',views.loginpage),
    path("login/", obtain_auth_token, name="login"),
    path("register/student/",views.student_registerpage,name="student_register"),
    path("login/<int:student_id>/",views.student_homepage,name="student_login"),
    path("home/<int:instructor_id>/",views.instructor_home,name="homepage"),

]

