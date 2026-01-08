from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("createuser/", views.creaetusers, name="createuser"),
    path("demoapi/", views.Demoapi.as_view(), name="demoapi"),
    path("userapi/", views.UsercustomeAPIView.as_view(), name="userapi"),
    path("login/", views.Userlogin.as_view(), name="login"),
    path("logout/", views.userlogout.as_view(), name="logout"),
    path('userprofiles/', views.Userprofile.as_view(), name='userprofiles'),
    path("me/", views.CurrentUserAPIView.as_view(), name="current-user"),
]
