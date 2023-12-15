from django.http import JsonResponse
from courses.models import Course,StudentCourse
from accounts.models import Profile
from django.views.decorators.csrf import csrf_exempt
from main.helpers.token import decode
import json
from datetime import datetime

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
         p = list(Course.objects
                  .filter(is_deleted = False)
                  .values("id","course_name","duration","description","instructor_name","course_fee","start_date"))
         output["data"] = p
        else:
         course = Course.objects.get(id=id,is_deleted = False)
         output["data"] = {
             "id":id,
             "course_name":course.course_name,
             "duration" :course.duration,
             "description" : course.description,
             "instructor_name" : course.instructor_name,
             "course_fee":course.course_fee,
             "start_date" : course.start_date
             
         }
         print(output)
    elif method == "POST":
        data = json.loads(request.body)
        print("json converted data from react",data)
        course_data = {
            "course_name":data["course_name"],
            "course_fee":data["course_fee"],
            'duration':data['duration'],
            'description':data['description'],
            'instructor_name':data['instructor_name'],
            'start_date':data['start_date'], 
 
        }
        courseFind = Course.objects.filter(course_name=course_data["course_name"],is_deleted = False)
        if courseFind :
            output["message"] = f"course with this name  {course_data['course_name']} already exist"
        else : 
            p = Course(**course_data)
            p.save()
            output['data'] = list(Course.objects
                  .filter(is_deleted = False)
                  .values("id","course_name","duration","description","instructor_name","course_fee","start_date"))
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
            p = list(Course.objects
                  .filter()
                  .values("id","course_name","duration","description","instructor_name","course_fee","start_date"))
            print(p)
            output["data"] = p
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

@csrf_exempt
def StudentCourseAPiView (request):
    output = {"data":None}
    method = request.method
    if method =="GET":
        p = list(StudentCourse.objects.filter().values("id","student_id","course_id" ,"student__first_name","course__course_name"))
        data=[]
        for item in p:
            item["first_name"] = item.pop("student__first_name")
            item["course_name"] = item.pop("course__course_name")
            data.append(item)
              
        output["student_courses"] = data
        output["courses"] = list(Course.objects.filter().values("id","course_name"))
        output["students"] = list(Profile.objects.filter().values("id","first_name"))

    elif method == "POST":
        data = json.loads(request.body)
        print("the data is ",data)
        studentCourseData ={
            "student_id": data["student_id"],
            "course_id": data["course_id"]

        }
        result = StudentCourse.objects.filter(student_id = studentCourseData["student_id"],course_id = studentCourseData["course_id"])
        if result :
            output["message"] =f"student with same {result['course_id']}has already taken the same course"
            output["status"] = 400
        else :
            try:
                
                sc = StudentCourse(
                student_id = studentCourseData["student_id"],
                course_id = studentCourseData["course_id"],
                registration_date = datetime.now())
                sc.save()
                output["message"] = "student enrolled"
                output["status"] = 200
            except Exception as e:
                output["status"] = 400
                output["message"] = "student enrollment failed"


        
        # p = list(StudentCourse.objects.filter().values("id","student_id","course_id" ,"student__first_name","course__course_name"))
        # sc = []
        # for item in p:
        #     item["first_name"] = item.pop("student__first_name")
        #     item["course_name"] = item.pop("course__course_name")
        #     sc.append(item)
              
        # output["student_courses"] = sc 
        # output["courses"] = list(Course.objects.filter().values("id","course_name"))
        # output["students"] = list(Profile.objects.filter().values("id","first_name"))
    elif method == "PATCH":
        print("doing patch")
    elif method == "DELETE":
        print("doing delete")

    return JsonResponse(output)