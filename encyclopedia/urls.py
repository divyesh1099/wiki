from django.urls import path

from . import views
app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("random", views.random, name="random"),
    path("wiki/<str:querry>", views.wikititle, name="wikititle"),
]
