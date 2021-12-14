from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import SignUpView

app_name= 'apps.blog_auth'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('register', SignUpView.as_view(),name='register'),
    path('registercomplete', TemplateView.as_view(
        template_name='registration/registercomplete.html'
    ),name='registercomplete'),
]