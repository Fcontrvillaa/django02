

from django.urls import path
from .views import RegistroUsuario, LoginUsuario
#from django.contrib.auth import views as v


urlpatterns = [
    
    path("registro/", RegistroUsuario.as_view, name="registro"),
    path("login/", LoginUsuario.as_view, name="login"),
    path("logout/", LoginUsuario.as_view(), name="logout"),
]
