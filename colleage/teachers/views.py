from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Teacher
from .forms import TeacherForm


@login_required
def teachers_view(request):
    """
    :param request:
    :return: list of teachers to logged in user, login form instead.
    """
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers/teacher_list.html', context)


