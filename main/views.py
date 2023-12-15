from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from accounts.models import Profile
from courses.models import Course
from main.helpers.token import encode
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# def HomeView(request):
#     total_student= 0
#     total_course= 0
#     # total_student = len(Profile.objects.all())
#     total_student = Profile.objects.count()
#     total_course = Course.objects.count()
#     output=f"""
#     Total student={total_student} ,
#     Total course = {total_course}    
#     """
#     return HttpResponse(output)
    
#with html response
def HomeView(request):
    total_student= 0
    total_course= 0
    # total_student = len(Profile.objects.all())
    total_student = Profile.objects.count()
    total_course = Course.objects.count()
    output={
        "total_student":total_student,
        "total_course" :total_course
    }

    return render(request,"index.html",output)

@csrf_exempt
def getToken(request):
    data = json.loads(request.body)
    print(data)
    p = Profile.objects.filter(
        email = data['email'],
        password = data['password']
    )
    if not p : 
        return JsonResponse({"message":["Invalid login crediantials"]})
    p = p.first()
    payload = {
        "id":p.id,
        "first_name":p.first_name
    }
    token = encode(payload)
    return JsonResponse({"data":{"token":token}})