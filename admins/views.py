from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView


from electronics.models import ElectronicApplicant


class SignInView(LoginView):
    template_name = 'admins/login.html'
    success_url = reverse_lazy('applicants-list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
            return self.form_invalid(form)
        
        return super().post(request, *args, **kwargs)


class SignOutView(LogoutView):
    template_name = 'admins/logout.html'

class ApplicantsListView(LoginRequiredMixin, ListView):
    model = ElectronicApplicant
    template_name = 'admins/applicants-list.html'


class ApplicantDetailView(LoginRequiredMixin, DetailView):
    model = ElectronicApplicant
    template_name = 'admins/applicant-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills = []
        obj = self.object

        if obj.altium_designer:
            skills.append('آلتیوم دیزاینر')
        elif obj.arduino:
            skills.append('آردوینو')
        elif obj.code_vision:
            skills.append('کد ویژن')
        elif obj.atmel_studio:
            skills.append('اتمل استودیو'),
        elif obj.micro_controller:
            skills.append('میکروکنتلر')
        elif obj.power:
            skills.append('منابع تغذیه')
        else:
            skills.append('ندارد')
        
        context['skills'] = skills
        file_name = None

        if obj.resume:
            path = obj.resume.url
            sections = path.split('/')
            file_name = sections[len(sections) - 1]
        
        context['filename'] = file_name

        return context


class ApplicantDeleteView(LoginRequiredMixin, DeleteView):
    model = ElectronicApplicant
    template_name = 'admins/delete-applicant.html'
    success_url = reverse_lazy('applicants-list')


@login_required
def download(request, id):
    obj = ElectronicApplicant.objects.get(id=id)
    filename = obj.resume.path
    response = FileResponse(open(filename, 'rb'))
    return response