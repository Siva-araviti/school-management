from django.urls import path, re_path
from . import views
from django.conf.urls import url
app_name = 'students'

urlpatterns = [
    path('all/', views.students_view, name='all_student'),
    path('add/', views.add_student_view, name='add_student'),
    path('update/<int:pk>/', views.student_update_view.as_view(),
         name='update_student'),
    path('<int:pk>/detail/', views.student_detail_view.as_view(),
         name='student_details'),
    path('<int:pk>/delete/', views.student_delete_view, name='delete_student'),
    re_path('^csv/$', views.export_users_csv_view, name='export_users_details_csv'),
]
