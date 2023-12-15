from django.urls import path,include
from courses.api_view import CourseAPiView,StudentCourseAPiView
from rest_framework import routers

urlpatterns = [
    path('',CourseAPiView),
    path('<int:id>', CourseAPiView),
    path('studentcourses/',StudentCourseAPiView),

    

]