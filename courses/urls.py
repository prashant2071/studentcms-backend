from django.urls import path
from courses.views import ListCourseView,AddCourse,StudentCourses


urlpatterns = [
    path('',ListCourseView,name='courses-list'),
    path('course-add/',AddCourse,name='course-add'),
    path('student-course/',StudentCourses,name='student-course')

]