from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    photo = models.ImageField(upload_to='students',
                              default='studentavar.png')
    date_of_birth = models.DateField(blank=True, null=True)
    registration_number = models.CharField(max_length=6, unique=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    subject = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['registration_number']
