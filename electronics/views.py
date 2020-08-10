from .forms import ElectronicApplianceForm, UploadForm

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView


class ElectronicApplianceView(CreateView):
    form_class = ElectronicApplianceForm
    template_name = 'electronics/request.html'
    success_url = reverse_lazy('upload-resume-page')


class ElectronicResumeUpload(FormView):
    form_class = UploadForm
    template_name = 'electronics/upload-resume.html'

