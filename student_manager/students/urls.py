from django.urls import path
from .views import (
    add_student,
    student_success,
    student_list,
    edit_student,
    delete_student,
)

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('success/', student_success, name='student_success'),
    path('list/', student_list, name='student_list'),
    path('edit/<int:student_id>/', edit_student, name='edit_student'),  # ✅ edit URL
    path('delete/<int:student_id>/', delete_student, name='delete_student'),

]
