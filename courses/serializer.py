from courses.models import Course,StudentCourse
from rest_framework import serializers

class CourseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name','course_fee','duration','description','instructor_name','course_fee','start_date']
        #fields = '__all__'
        # exclude = [ 'description']
        
class StudentCourseSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(source='student.first_name')
    course = serializers.StringRelatedField(source='course.course_name')

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course','registration_date']