from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.nowels.as_view(), name="nowel"),
    path("<int:pk>/ubate", views.ubate.as_view(), name="ubate"),
    path("<int:pk>/delete", views.delete.as_view(), name="delete"),
    path("search/", views.Search.as_view(), name="search"),
]
