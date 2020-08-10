from .models import ElectronicApplicant, FileUpload

from applicants.models import DEGREE_CHOICES

from django import forms


CHAR_FIELD_ERROR_MESSAGES = {
    'required': 'وارد کردن این فیلد الزامیست',
    'max_length': 'تعداد کاراکتر بیش از حد مجاز',
    'min_length': 'تعداد کاراکتر کمتر از حد مجاز میباشد'
}

class ElectronicApplianceForm(forms.ModelForm):

    first_name = forms.CharField(
        label='نام',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 ml-sm-5 col-4' 
            }
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=45,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
    )

    national_id = forms.CharField(
        label='شماره ملی',
        max_length=10,
        min_length=10,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
    )

    age = forms.IntegerField(
        label='سن',
        min_value=18,
        max_value=65,
        widget=forms.NumberInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={
            'required': 'وارد کردن این فیلد الزامیست',
            'invalid': 'مقدار وارد شده معتبر نمیباشد',
            'min_value': ' کمتر از حد مجاز',
            'max_value': 'بیشتر از حد مجاز'
        }
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages={
            'required': 'وارد کردن این فیلد الزامیست',
            'invalid': 'معتبر نمیباشد',
            'unique': 'این ایمیل قبلا ثبت شده است'
        }
    )

    mobile_phone = forms.CharField(
        label='تلفن همراه',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2 ml-sm-5 col-4' }
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES.update({
            'unique': 'این شماره موبایل قبلا ثبت شده است'
        })
    )

    address = forms.CharField(
        label='آدرس',
        required=False,
        widget=forms.Textarea(
            attrs={'class' : "form-control col-10 mb-2 ml-sm-5"}
        )
    )

    university = forms.CharField(
        label='دانشگاه',
        max_length=80,
        widget=forms.TextInput(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
    )

    university_subject = forms.CharField(
        label='رشته تحصیلی',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
    )

    university_degree = forms.ChoiceField(
        label='مدرک تحصیلی',
        widget=forms.Select(
            attrs={'class' : "form-control mb-2 ml-sm-5 col-2"}
        ),
        choices=DEGREE_CHOICES,
    )

    work_reputations = forms.CharField(
        label='سوابق',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control col-12'}
            ),
        error_messages=CHAR_FIELD_ERROR_MESSAGES
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
    )

    resume = forms.FileField(
        max_length=1024*1024*8,
        allow_empty_file=True,
        required=False
    )

    expected_salary = forms.IntegerField(
        max_value=999999,
        min_value=1000,
        label='حقوق پیشنهادی',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control mb-3'}
        ),
        error_messages={
            'required': 'وارد کردن این فیلد الزامیست',
            'invalid': 'مقدار وارد شده معتبر نمیباشد',
            'min_value': ' کمتر از حد مجاز',
            'max_value': 'بیشتر از حد مجاز'
        }
    )
    
    class Meta:
        model = ElectronicApplicant
        fields = '__all__'
        #exclude = ('resume',)



class UploadForm(forms.ModelForm):

    file = forms.FileField(
        max_length=1024*1024*8,
        allow_empty_file=True,
        required=False
    )

    class Meta:
        model = FileUpload
        fields = '__all__'