from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("polo", views.index2, name="pol"),
    path("cot", views.cot, name="cot"),
    path("love", views.love, name="love"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("creat", views.create, name="creat"),
    # path("user/profile/<str:username>/", views.index2, name="user_profile"),
]
