from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile


def StudentView(request):
    total_student = Profile.objects.all()
    output={
        "students":total_student
    }    
    return render(request,"students.html",output)


def AddStudents(request):
    output={"message":"","success":""}
    method = request.method
    if method == 'POST':
        data = request.POST
        if len(data['phone'])!=10: 
         output['message'] ="length of phone must be 10"
         output['success'] = 'False' 
         return render (request,'addstudent.html',output)

        elif len(data['last_name']) <5: 
         output['message'] ="length of last name must be atleast 5 character"
         output['success'] = 'False' 
         return render (request,'addstudent.html',output)
        elif len(data['first_name']) <5: 
         output['message'] ="length of first name must be atleast 5 character"
         output['success'] = 'False'
        else:  
         profile_data = {
            'first_name':data['first_name'],
            'last_name':data['last_name'],
            'email':data['email'],
            'password':data['password'],
            'phone':data['phone'],
        }
         profile= Profile.objects.filter(email=profile_data['email'])
         if profile:
            output['message'] = f'Student with email :{profile_data["email"]} already exist'
            output['success'] = 'False'
         else:
            p=Profile(**profile_data)
            p.save()
            output['message'] =f"{profile_data['first_name']} Added successfully "
            output['success'] = 'True'
            
    
    return render (request,'addstudent.html',output)
