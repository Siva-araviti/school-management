from django.forms import ModelForm
from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo','date_of_birth','mobile']

