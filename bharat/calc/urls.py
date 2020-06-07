from django.urls import path
from . import views

urlpatterns = [
    path("hey", views.home, name="home"),
    path("add", views.add_num, name="addition"),
]