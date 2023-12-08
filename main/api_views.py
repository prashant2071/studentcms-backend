from accounts.models import Profile
from courses.models import Course
from django.http import JsonResponse


def HomeView(request):
    total_student= 0
    total_course= 0
    total_student = Profile.objects.count()
    total_course = Course.objects.count()
    output={
        "total_student":total_student,
        "total_course" :total_course
    }
    
    return JsonResponse(output)