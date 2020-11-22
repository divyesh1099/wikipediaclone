from django.urls import path
from . import views
app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),   
    path("search", views.search, name="search"),    
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("randompage", views.randompage, name="randompage"),
    path("wiki/<str:title>", views.wikititle, name="wikititle"),
]
