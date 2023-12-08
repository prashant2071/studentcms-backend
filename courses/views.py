from django.shortcuts import render
from courses.models import Course ,StudentCourse
from accounts.models import Profile
from datetime import datetime

# Create your views here.
def ListCourseView(request):
    courses=Course.objects.all()
    return render (request,"courses.html",{"courses":courses})

def AddCourse (request):
    output={"message":"","success":""}
    method = request.method
    if method == 'POST':
        data = request.POST

        if len(data['instructor_name']) <5: 
         output['message'] ="length of last name must be atleast 5 character"
         output['success'] = 'False' 
         return render (request,'addcourse.html',output)
        else:  
         course_data = {
            'course_name':data['course_name'],
            'duration':data['duration'],
            'description':data['description'],
            'instructor_name':data['instructor_name'],
            'course_fee':data['course_fee'],
            'start_date':data['start_date'],

        }
        p=Course(**course_data)
        p.save()
        output['message'] =f"{course_data['course_name']} Added successfully "
        output['success'] = 'True'
            
    return render (request,"addcourse.html",output)
    
def StudentCourses(request):
    output={}
    if request.method== 'POST':
        course_id = request.POST['course']
        student_id = request.POST['student']
        
        sc = StudentCourse.objects.filter(
            student_id = student_id,
            course_id = course_id,
        )
        
        if sc:
            output['message'] = 'Already enrolled'
        else:
            sc = StudentCourse(
                student_id = student_id,
                course_id = course_id,
                registration_date = datetime.now()
  
            )
            sc.save()
    output["courses"] = Course.objects.filter().values('id',"course_name")
    output["students"] = Profile.objects.filter().values('id',"first_name")
    output["student_courses"] = StudentCourse.objects.filter().values('student__first_name', 'course__course_name')    
    return render (request,"studentcourse.html",output)
    
     
    
    
