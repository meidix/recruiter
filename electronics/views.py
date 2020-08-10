from .forms import ElectronicApplianceForm, UploadForm
from .models import ElectronicApplicant

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView


class ElectronicApplianceView(CreateView):
    model = ElectronicApplicant
    form_class = ElectronicApplianceForm
    template_name = 'electronics/request.html'
    success_url = reverse_lazy('electronic-resume-upload-form')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            request.session['nat_id'] = form.cleaned_data.get('national_id')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ElectronicResumeUpload(FormView):
    form_class = UploadForm
    template_name = 'electronics/upload-resume.html'
    success_url = reverse_lazy('index-page')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            resume = request.FILES.get('resume')
            national_id = request.session['nat_id']
            user = ElectronicApplicant.objects.filter(national_id=national_id).first()
            request.session.pop('nat_id')
            user.resume = resume
            messages.success(request, 'رزومه با موفقیت بارگذاری شد')
            return self.form_valid(form)
        
        messages.error(request, 'فایلی آپلود نشده')
        return self.form_invalid(form)
         

