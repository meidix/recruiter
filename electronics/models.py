from applicants.models import Applicant

from django.db import models


class FileUpload(models.Model):
    file = models.FileField(null=True, blank=True)


class ElectronicApplicant(Applicant):
    altium_designer = models.BooleanField(blank=True, default=False)
    arduino = models.BooleanField(blank=True, default=False)
    code_vision = models.BooleanField(blank=True, default=False)
    proteus = models.BooleanField(blank=True, default=False)
    atmel_studio = models.BooleanField(blank=True, default=False)
    micro_controller = models.BooleanField(blank=True, default=False)
    power = models.BooleanField(null=True, blank=True, default=False)
    others = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='tmp/resume', null=True, blank=True)
    #resume = models.ForeignKey('FileUpload', on_delete=models.SET_NULL, null=True, blank=True)
    expected_salary = models.FloatField(blank=True, null=True)