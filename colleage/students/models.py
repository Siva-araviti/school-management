from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    photo = models.ImageField(upload_to='students',
                              default='studentavar.png')
    date_of_birth = models.DateField(blank=True, null=True)
    registration_number = models.CharField(max_length=6, unique=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField(null=True, blank=True, default=None)
    paid_amount = models.FloatField(null=True, blank=True, default=None)
    due_amount = models.FloatField(null=True, blank=True, default=None)
    add_amount = models.FloatField(null=True, blank=True, default=None)
    # def __str__(self):
    #     return '{} ({}) semester {} dept.'.format(
    #         self.name
    #     )

    class Meta:
        ordering = ['registration_number']


