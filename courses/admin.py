from django.contrib import admin
from courses.models import Course, StudentCourse

# admin ko model ho vanera inform gareko
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "course_name","duration","instructor_name","course_fee","start_date","custom_feild"]
    
    # this is custum feild for like multiplying price and quantity 2*5=10 
    def custom_feild(self,obj):
        return f"Feild :{obj.id}"
    
    # yo rakhiyoo vane listed field name matri change garna dinxa
    # fields=["course_name","instructor_name"]
    
    #we can use exclude only course_name if course name is in list
    # exclude = ["course_name"]

# course ma courseadmin register gareko
admin.site.register(Course, CourseAdmin)


class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ["id","student","course","registration_date"]
    
    #course_id student_id rakhiyoo vane id integer value noi aauxa
    # list_display = ["id","student_id","course_id","registration_date"]


#studentCourse admin 
admin.site.register(StudentCourse, StudentCourseAdmin)

# Register your models here.
