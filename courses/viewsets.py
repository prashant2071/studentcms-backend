from rest_framework import viewsets
from rest_framework.response import Response 
from courses.models import Course,StudentCourse
from courses.serializer import CourseSerializer,StudentCourseSerializer
 
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    
class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class =  StudentCourseSerializer
    queryset = StudentCourse.objects.all()

