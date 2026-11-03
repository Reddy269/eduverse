from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('<int:id>/',views.homepage,name='homepage'),
    path('<int:id>/in_draft/',views.homepage,name='homepage'),
    path('<int:id>/draft/<int:course_id>',views.homepage,name='homepage'),
    path('<int:id>/completed/',views.homepage,name='homepage'),
    path('<int:id>/listed/',views.homepage,name='homepage')
]