from django.urls import path
from . import views

urlpatterns = [
    path('/login', views.authentication, name="login"),
    path('/logout', views.sign_out, name="logout"),
]
