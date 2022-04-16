from django.shortcuts import render
from django.views.generic import TemplateView


class AuthGithub(TemplateView):
    template_name = 'auth/oauth.html'


class HomeView(TemplateView):
    template_name = 'store/home.html'
