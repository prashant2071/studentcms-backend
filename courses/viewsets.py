from rest_framework import viewsets,serializers
from rest_framework.response import Response 
from courses.models import Course,StudentCourse
from courses.serializer import CourseSerializer
 
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        data.append({"message":"this is pagination"})
        return Response(data)

class StudentCourseSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(source='student.first_name')
    course = serializers.StringRelatedField(source='course.name')

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course']