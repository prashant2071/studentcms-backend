from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Profile
from main.helpers.token import decode
import json


@csrf_exempt
def StudentAPiView (request ,id=None):
    output = {"data":None,"message":""}
    print("======================token============")
    token = request.META['HTTP_AUTHORIZATION']
    print("the decoded is ",token)
    decoded = decode(token)
    if decoded == False:
        output["message"] = "Unauthorized"
        return JsonResponse(output)
    method = request.method
    if method =="GET":
        if id is None:
         print("========================= GET ================")
        #  p = list(Profile.objects.filter().values("id","first_name"))
         p = list(Profile.objects.filter().values("id","first_name","last_name","email","password","phone"))
         print(p)
         output["data"] = p
         output["message"] = "data fetched successfully"
        else:
         student = Profile.objects.get(id=id)
         output["data"] = {
             "id":id,
             "first_name":student.first_name
         }
    elif method == "POST":
        data = json.loads(request.body)
        print("json converted data from react",data)
        # for form data
        # data = request.POST
        profile_data = {
            "first_name":data["first_name"],
            "last_name":data["last_name"],
            "email":data["email"],
            'password':data['password'],
            'phone':data['phone'],  
        }
        profile = Profile.objects.filter(email=profile_data["email"])
        if profile :
            output["message"] = f"student with email {profile_data['email']} already exist"
        else : 
            p = Profile(**profile_data)
            p.save()
            output["data"] = list(Profile.objects.filter().values("id","first_name","last_name","email","password","phone"))
            output['message'] =f"{profile_data['first_name']} Added successfully "

    elif method == "PATCH":
        print("----------- patch method ------------------")
        data = json.loads(request.body)
        print("the data is",data,"the id is",id)
        p=Profile.objects.filter(id=id)
        print("the data of p is",p)
        if not p:
            output["message"] = f"student {id} not found"
        else:
            data_to_update={}
            feilds=['first_name',"last_name","phone","email","password",]
            for feild in feilds:
                print(data.get(feild))
                if data.get(feild):
                    data_to_update[feild] = data.get(feild)
            p.update(**data_to_update)
            output["data"] = list(Profile.objects.filter().values("id","first_name","last_name","email","password","phone"))
            output["message"] = "data updated successfully"
        # data = request.POST
        # p = Profile.objects.filter(id=id)
        # p.update(**data)
        # output["data"] = p
        # output["message"] ="data updated successfully"
        
        
    elif method == "DELETE":
        if id :
            try:
              p = Profile.objects.get(id=id)
              print(f"the id is {id}",p)
            #   output["data"] =  p
              p.delete()
              output["message"] = "data delete successfully"
            except Exception as e:
              output["message"] = f"failed to delete data {e} "
        else:
            output["message"] = "Please provide user id"
 
    return JsonResponse(output)