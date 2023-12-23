from rest_framework import viewsets,status
# from rest_framewor     
# k.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import json
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from courses.models import Course,StudentCourse
from courses.serializer import CourseSerializer,CourseDetailsSerializer,CourseCreateSerializer,CoursePatchSerializer,StudentCourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class CourseViewSet(viewsets.ModelViewSet):
    # serializer_class = CourseSerializer
    # queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset,many=True)
        course = serializer.data
        return Response(course,status=status.HTTP_200_OK)
        

    def retrieve(self, request, pk):
        course = Course.objects.get(id=pk)
        #course = get_object_or_404(course, pk)
        serializer = CourseDetailsSerializer(course)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self ,request):
        data = request.data
        serializers = CourseCreateSerializer(data=data)
        if(serializers.is_valid()):
            course = Course.objects.create(**serializers.data)
            data = serializers.data
            data["id"] = course.id
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        data = request.data
        serializer = CoursePatchSerializer(data=data)
        if not serializer.is_valid():
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            course = Course.objects.filter(id=pk)
            course.update(**serializer.data)
            return Response(data , status=status.HTTP_200_OK)
    
    def destroy (self,request,pk):
        course = Course.objects.get(id=pk)
        course.delete()
        return Response({},status = status.HTTP_200_OK )
    
    
    
class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class =  StudentCourseSerializer
    queryset = StudentCourse.objects.all()

