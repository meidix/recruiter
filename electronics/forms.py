from .models import ElectronicApplicant

from applicants.models import DEGREE_CHOICES

from django import forms


class ElectronicApplianceForm(forms.ModelForm):

    first_name = forms.CharField(
        label='نام',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 ml-sm-5 col-4' 
            }
        ),
        error_messages={}
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=45,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={}
    )

    national_id = forms.CharField(
        label='شماره ملی',
        max_length=10,
        min_length=10,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={}
    )

    age = forms.IntegerField(
        label='سن',
        widget=forms.NumberInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={}
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={}
    )

    mobile_phone = forms.CharField(
        label='تلفن همراه',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={}
    )

    address = forms.CharField(
        label='آدرس',
        required=False,
        widget=forms.Textarea(
            attrs={'class' : "form-control col-10 mb-2 ml-sm-5"}
        ),
        error_messages={}
    )

    university = forms.CharField(
        label='دانشگاه',
        max_length=80,
        widget=forms.TextInput(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        error_messages={}
    )

    university_subject = forms.CharField(
        label='رشته تحصیلی',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        error_messages={}
    )

    university_degree = forms.ChoiceField(
        label='مدرک تحصیلی',
        max_length=15,
        widget=forms.Select(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        choices=DEGREE_CHOICES,
        error_messages={}
    )

    work_reputations = forms.CharField(
        label='سوابق',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control col-12'}
            ),
        error_messages={}
    )

    altium_designer = forms.BooleanField(
        label='آلیتوم دیزانیر(altium designer)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    arduino = forms.BooleanField(
        label='آردوینو(arduino)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    code_vision = forms.BooleanField(
        label='کد ویژن (Code vision)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    proteus = forms.BooleanField(
        label=' پروتئوس(proteus)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    atmel_studio = forms.BooleanField(
        label=' اتمل استودیو(Atmel studio)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    micro_controller = forms.BooleanField(
        label=' میکرو کنترلر',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    power = forms.BooleanField(
        label='مدارات تغذیه',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input mb-2 mr-1 ml-lg-5'}
        ),
    )

    others = forms.CharField(
        label='مهارت های دیگر',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control col-12'}
        ),
        required=False
    )

    expected_salary = forms.DecimalField(
        max_value=999999,
        min_value=1000,
        label='حقوق پیشنهادی',
        required=False,
        wdiget=forms.NumberInput(
            attrs={'class': 'form-control mb-3'}
        ),
        required=False
    )
    
    class Meta:
        model = ElectronicApplicant
        fields = '__all__'
        exclude = 'resume'



class UploadForm(forms.ModelForm):

    resume = forms.FileField(
        max_length=1024*1024*8,
        allow_empty_file=True,
        required=False
    )

    class Meta:
        model = ElectronicApplicant
        fields = ['resume']