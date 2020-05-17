from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('all/', views.teachers_view, name='all_teacher'),

]
