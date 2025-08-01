from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .form import FormularioRegistroUsuario

# Create your views here.

""" 
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
       form = UserCreationForm()         
    return render(request, "usuarios/registro.html", {"form": form})
 """

class RegistroUsuario(SuccessMessageMixin, CreateView): #registro
    form_class = FormularioRegistroUsuario
    template_name = "usuarios/registro.html"
    success_url = reverse_lazy('login')
    success_message = 'usuario registrado correctamente'

class LoginUsuario(LoginView):                  # login
    template_name = 'usuarios/login.html'

class LogoutUsuario(LoginRequiredMixin, LogoutView):   #mixin logout view
    next_page = reverse_lazy('home')      #pagina a la que va
    http_method_names = ['get','post']