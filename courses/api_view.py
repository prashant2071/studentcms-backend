from django.http import JsonResponse
from courses.models import Course,StudentCourse
from django.views.decorators.csrf import csrf_exempt
from main.helpers.token import decode
import json

# @csrf_exempt
# def CourseAPiView (request,id=None):
#     print("hahah----------------------------------------")
#     output = {"data":[]}
#     method = request.method
#     if method =="GET":
#         if id is None:
#          p = list(Course.objects.filter().values("id","course_name"))
#          output["data"] = p
#         else:
#          course = Course.objects.get(id=id)
#          output["data"] = {
#              "id":id,
#              "course_name":course.course_name
#          }
#     elif method == "POST":
#         data = json.loads(request.body)
#         print("json converted data")
#         # for form data
#         # data = request.POST
#         course_data = {
#             "course_name":data["course_name"],
#             "course_fee":data["course_fee"],
#             'duration':data['duration'],
#             'description':data['description'],
#             'instructor_name':data['instructor_name'],
#             'start_date':data['start_date'], 
 
#         }
#         course = Course.objects.filter(course_name=course_data["course_name"])
#         if course :
#             output["message"] = f"course with this name  {course_data['course_name']} already exist"
#         else : 
#             p = Course(**course_data)
#             p.save()
#             output['message'] =f"{course_data['course_name']} Added successfully "
#     elif method == "PATCH":
#         p = Course.objects.filter()
#         print("doing patch")
#     elif method == "DELETE":
#         print("doing delete")

#     return JsonResponse(output)

@csrf_exempt
def CourseAPiView (request,id=None):
    
    output = {"data":None,"messages":[]}
    token = request.META['HTTP_AUTHORIZATION']
    decoded = decode(token)
    if decoded == False:
        output["message"] = "Unauthorized"
        return JsonResponse(output)
    method = request.method
    if method =="GET":
        if id is None:
         p = list(Course.objects.filter().values("id","course_name"))
         output["data"] = p
        else:
         course = Course.objects.get(id=id)
         output["data"] = {
             "id":id,
             "course_name":course.course_name
         }
    elif method == "POST":
        data = json.loads(request.body)
        print("json converted data")
        # for form data
        # data = request.POST
        course_data = {
            "course_name":data["course_name"],
            "course_fee":data["course_fee"],
            'duration':data['duration'],
            'description':data['description'],
            'instructor_name':data['instructor_name'],
            'start_date':data['start_date'], 
 
        }
        profile = Course.objects.filter(email=course_data["course_name"])
        if profile :
            output["message"] = f"course with this name  {course_data['course_name']} already exist"
        else : 
            p = Course(**course_data)
            p.save()
            output['message'] =f"{course_data['course_name']} Added successfully "
       
    elif method == "PATCH":
        print("----------- patch method ------------------")
        data = json.loads(request.body)
        p=Course.objects.filter(id=id)
        if not p:
            output["message"] = f"Course {id} not found"
        else:
            data_to_update={}
            feilds=['course_fee',"duration","instructor_name","start_date","description"]
            for feild in feilds:
                if data.get(feild):
                    data_to_update[feild] = data.get(feild)
            p.update(**data_to_update)
            output["message"] = "data updated successfully"
    elif method == "DELETE":
        print("-------delete method --------")
        if id :
            try:
              p = Course.objects.get(id=id)
              print(p)
              p.delete()
              output["message"] = "data delete successfully"
            except Exception as e:
              output["message"] = f"{e}"
            else:
                output["message"] = "no course found"
        else:
            output["message"] = "Please provide course id"

    return JsonResponse(output)

def StudentCourseAPiView (request):
    output = {"data":None}
    method = request.method
    if method =="GET":
        p = list(StudentCourse.objects.filter().values("id","student__first_name","course__course_name"))
        data=[]
        for item in p:
            
            item["first_name"] = item.pop("student__first_name")
            item["course_name"] = item.pop("course__course_name")
            data.append(item)
              
        output["data"] = data
    elif method == "POST":
        print("doing post")
    elif method == "PATCH":
        print("doing patch")
    elif method == "DELETE":
        print("doing delete")

    return JsonResponse(output)