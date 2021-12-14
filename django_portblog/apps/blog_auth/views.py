from django.forms.forms import Form
from django.shortcuts import render

from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView

from .models import Profile

from .forms import SignUpForm

# Create your views here.

class Login(auth_views.LoginView):
    ''' Vista de Login de Usuario '''
    template_name = 'login.html'

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    ''' Vista de Logout/Cierre sesión de Usuario '''
    template_name = 'logged_out.html'


class SignUpView(FormView):
    ''' Vista de registro de usuario'''
    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('blog_auth:registercomplete')

    def form_valid(self, form):
        ''' Verificamos que los datos sean válidos y los guardamos'''
        form.save()
        return super().form_valid(form)
        


class WelcomeView(CreateView):
    template_name = 'welcome.html'