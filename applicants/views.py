from django.shortcuts import render
from django.views.generic.base import TemplateView


class indexView(TemplateView):
    template_name = 'applicants/index.html'


class AboutView(TemplateView):
    template_name = 'applicants/about.html'
