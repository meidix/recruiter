from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


def SignInView(LoginView):
    template_name = 'admins/login.html'


def SignOutView(LogoutView):
    template_name = 'admins/logout.html'