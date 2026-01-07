from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("createuser/", views.creaetusers, name="createuser"),
    path("userapi/", views.UsercustomeAPIView.as_view(), name="userapi"),
    path("login/", views.Userlogin.as_view(), name="login"),
    path("logout/", views.userlogout.as_view(), name="logout"),
]
