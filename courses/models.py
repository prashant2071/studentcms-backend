from django.db import models

from accounts.models import Profile


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description = models.TextField(null=True)
    instructor_name = models.CharField(max_length=255)
    course_fee = models.IntegerField()
    start_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default = False) 

    def __str__(self):
        return self.course_name


class StudentCourse(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField()

    def __str__(self):
        return f"{self.student.email} ==> {self.course.course_name}"
