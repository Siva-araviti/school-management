from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'])
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.save()
        # teacher_profile = TeacherProfile.objects.create(user=user, school=self.cleaned_data['school'],
        #                                                 subject=self.cleaned_data['subject'],
        #                                                 head_of_subject=self.cleaned_data['head_of_subject'])
        return user

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password didn\'t match!')
        return cd['password2']