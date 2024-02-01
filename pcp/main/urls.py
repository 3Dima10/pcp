from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("polo", views.index2, name="pol"),
    path("cot", views.cot, name="cot"),
]
