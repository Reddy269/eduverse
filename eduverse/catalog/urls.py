from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('<str:user_id>/',views.homepage,name='homepage'),
    path('onboarding/<str:username>/',views.onboarding,name='onboarding'),
    path('<str:id>/in_draft/',views.homepage,name='homepage'),
    path('<str:id>/draft/<int:course_id>',views.homepage,name='homepage'),
    path('<str:id>/completed/',views.homepage,name='homepage'),
    path('<str:id>/listed/',views.homepage,name='homepage')
]