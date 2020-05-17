from .models import Student
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import (Layout, Fieldset, Field,
                                 ButtonHolder, Submit, Div)

from django.contrib.auth.models import User
from .models import Student
import django_filters

class StudentForm(forms.ModelForm):
    username = forms.CharField(label='User Name',
                               widget=forms.TextInput)
    first_name = forms.CharField(label='First Name',
                                widget=forms.TextInput)
    email = forms.CharField(label='Email',
                                 widget=forms.TextInput)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password1',
                                 widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'photo',
            'date_of_birth',
            'registration_number',
            'mobile',
            'total_amount','paid_amount','due_amount','add_amount',
            'username', 'first_name', 'email', 'password', 'password1'
        ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab('Student Personal Info',
                    'username',
                    'first_name',
                    'email',
                    'password',
                    'password1',
                    css_class="extra"),
                Tab('Student Register Info',
                    'photo',
                    'date_of_birth',
                    'registration_number',
                    'mobile',
                    ),
                Tab('Student Payment Info',
                    Field('total_amount',
                          'paid_amount',
                          'due_amount',
                          ButtonHolder(
                              Submit('submit', 'Admit Student',
                                     css_class='float-right btn-dark mr-3')
                          ),
                          css_class="extra"),
                    ),
            ),
        )

    def save(self):

        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'])
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.save()
        student_profile = Student.objects.create(user=user, photo=self.cleaned_data['photo'],
                                                        date_of_birth=self.cleaned_data['date_of_birth'],
                                                        mobile=self.cleaned_data['mobile'],
                                                        registration_number=self.cleaned_data['registration_number'],
                                                        total_amount=self.cleaned_data['total_amount'],
                                                        paid_amount=self.cleaned_data['paid_amount'],
                                                        due_amount=self.cleaned_data['due_amount'])
        return user, student_profile

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password didn\'t match!')
        return cd['password2']

