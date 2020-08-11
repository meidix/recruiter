from .forms import ElectronicApplianceForm
from .models import ElectronicApplicant

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView


class ElectronicApplianceView(CreateView):
    model = ElectronicApplicant
    form_class = ElectronicApplianceForm
    template_name = 'electronics/request.html'
    success_url = reverse_lazy('electronic-success')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            request.session['nat_id'] = form.cleaned_data['national_id']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ApplicanceSuccessView(TemplateView):
    template_name = 'electronics/success.html'
    nat_id = None

    def dispatch(self, request, *args, **kwargs):
        self.nat_id = request.session['nat_id']
        request.session.pop('nat_id')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicant = ElectronicApplicant.objects.filter(national_id=self.nat_id).first()
        context['appl'] = applicant
        return context


         

