from courses.models import Course,StudentCourse
from rest_framework import serializers

# class CourseSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['course_name','course_fee','duration','description','instructor_name','course_fee','start_date']
#         #fields = '__all__'
#         # exclude = [ 'description']
 
 
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    course_name = serializers.CharField()
    duration = serializers.CharField()
 
 
class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model:Course
        exclude = ["is_deleted"]

class CourseCreateSerializer(serializers.Serializer):
     id = serializers.ReadOnlyField()
     course_name = serializers.CharField(required = True)
     duration = serializers.CharField(required = True)
     description = serializers.CharField(required=False)
     course_fee = serializers.CharField(required = True)
     start_date = serializers.DateField(required = True)
     instructor_name = serializers.CharField(required= True)
     is_deleted = serializers.BooleanField(default=False)
      
class CoursePatchSerializer(serializers.Serializer):
     course_name = serializers.CharField(required = False)
     duration = serializers.CharField(required = False)
     description = serializers.CharField(required=False)
     course_fee = serializers.CharField(required = False)
     start_date = serializers.DateTimeField(required = False)
     instructor_name = serializers.CharField(required= False)
     is_deleted = serializers.BooleanField(default=False)
       
class StudentCourseSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(source='student.first_name')
    course = serializers.StringRelatedField(source='course.course_name')

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course','registration_date']