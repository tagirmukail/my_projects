"""Определяет url для пользователей"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # страница входа.
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # страница выхода.
    url(r'^logout/$', views.logout_view, name='logout'),
    # страница регистрации.
    url(r'^register/$', views.register, name='register'),
]