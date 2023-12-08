from django.urls import path
from courses.api_view import CourseAPiView,StudentCourseAPiView

urlpatterns = [
    path('',CourseAPiView),
    path('<int:id>', CourseAPiView),
    path('studentcourse/',StudentCourseAPiView),

    

]