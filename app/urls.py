
from django.urls import path
from .views import home, about

urlpatterns = [
    
    path("", home, name="app/home"),
    path("about/", about, name="about"),
]
