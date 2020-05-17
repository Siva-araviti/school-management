from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Student
from .forms import StudentForm
import csv
from send_mail.email import send_email
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required
def add_student_view(request):
    """
    :param request:
    :return: admission form to
    logged in user.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user, student = form.save()
            assign_role(user, 'student')
            # :send mail section

            # html_message = render_to_string('students/email.html',
            #                                 {'username': form.cleaned_data.get("username"),
            #                                  'password': form.cleaned_data.get("password")})
            # plain_message = strip_tags(html_message)
            # send_email("Student Credentials", plain_message, (user.email,))
            pk = form.instance.pk
            return render(request, 'students/student_sucess.html')
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'students/addstudent.html', context)

@login_required
def students_view(request):
    """
    :param request:
    :return: renders student list with all department
    and semesters list.
    """
    all_students = Student.objects.all()
    context = {'students': all_students}
    return render(request, 'students/students_list.html', context)

class student_detail_view(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = kwargs['object']
        pk = obj.id
        student = Student.objects.get(pk=pk)
        # get student object
        # for showing subjects in option form
        # student_subject_qs = student.has_subjects()[0]
        # student_subject_qs = student_subject_qs.subjects.all()
        # context['subjects'] = student_subject_qs
        # getting result objects
        # semesters = range(1, student.semester.number + 1)
        context['student'] = student
        return context

class student_update_view(LoginRequiredMixin, UpdateView):
    """
    renders a student update form to update students details.
    """
    model = Student
    fields = ['photo','mobile', 'total_amount', 'paid_amount', 'due_amount']
    template_name = 'students/update_student.html'

    def get_success_url(self):
        student_id = self.kwargs['pk']
        return reverse_lazy('students:student_details', kwargs={'pk': student_id})




@login_required
def student_delete_view(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('students:all_student')



def export_users_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Email address','Mobile', 'Total Fee','Paid amount','Due amount'])

    students = Student.objects.all()
    # users = User.objects.all().values_list('username', 'first_name', 'email')
    for student in students:
        user_data = [student.user.username, student.user.first_name, student.user.email,
                     student.mobile, student.total_amount, student.paid_amount, student.due_amount]
        writer.writerow(user_data)

    return response


