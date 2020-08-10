from django.db import models

DEGREE_CHOICES =[
    ('diploma', 'دیپلم'),
    ('bachelor', 'کارشناسی'),
    ('senior', 'کارشناسی ارشد'),
    ('phd', 'دکتری')
]

class Applicant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=45)
    national_id = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(max_length=11, unique=True)
    address = models.TextField(blank=True, null=True)
    university = models.CharField(max_length=80)
    university_subject = models.CharField(max_length=50)
    university_degree = models.CharField(choices=DEGREE_CHOICES, max_length=15)
    work_reputations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} { self.last_name}'

    class Meta:
        abstract = True