from django.urls import path
from accounts.views import StudentView,AddStudents

urlpatterns = [
    path('',StudentView,name='students-list'),
    path('student-add/',AddStudents,name='student-add'),
]