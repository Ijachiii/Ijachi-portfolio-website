from . import views
from django.urls import path
from .models import Contact


urlpatterns = [
    path("", views.home, name="home"),

]