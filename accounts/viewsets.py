from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import json
from rest_framework.parsers import FileUploadParser

from main.helpers.hash import hash_file
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import os
import time


from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Profile
from rest_framework.response import Response
from accounts.serializer import ProfileSerializer,ProfileDetailSerializer,ProfileCreateSerializer,ProfilePatchSerializer
from django.conf import settings
# class ProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @method_decorator(cache_page(60))
    def list(self,request):
        profiles = settings.REDIS_CLIENT.get('profile')
        print("getting student list---------")
        if profiles:
            print("Returning from profile")
            profiles = json.loads(profiles)
        else:
              
          queryset = Profile.objects.all()
          serializer = ProfileSerializer(queryset, many=True)
          profiles = serializer.data
          # for profile in Profiles:
          #     print(profile)
          settings.REDIS_CLIENT.set('profile',json.dumps(profiles))
        return Response(profiles)
    
    def retrieve (self,request,pk):
        profile = Profile.objects.get(id=pk)
        print("======================id========= is",id)
        # profile = get_object_or_404(profile,pk)
        serializer  = ProfileDetailSerializer(profile)
        return Response(serializer.data)
    @swagger_auto_schema(
        request_body=ProfileCreateSerializer
    )
    def create(self,request):
        data = request.data
        serializer = ProfileCreateSerializer(data=data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            profile = Profile.objects.create(**serializer.data)
            data = serializer.data
            data["id"] = profile.id
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def partial_update (self, request, pk):
        data = request.data
        serializer = ProfilePatchSerializer(data=data)
        if not serializer.is_valid():
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        else:
            profile = Profile.objects.filter(id=pk)
            profile.update(**serializer.data)
            return Response(data,status= status.HTTP_200_OK)
    
    def destroy (self, request, pk):
        profile = Profile.objects.get(id=pk)
        profile.delete()
        return Response({},status=status.HTTP_204_NO_CONTENT)
    
class FileUploadView(APIView):

    parser_classes = [FileUploadParser]
    authentication_classes = [JWTAuthentication]

    def post(self, request, filename):
        output = {"message": ""}
        print("inside post")
        file = request.data['file']
        print(file)
        print(vars(file))
        print(file.name)

        now_time = str(time.time()).replace(".", "")
        path = settings.UPLOAD_PATH + "/" + now_time + file.name
        temp_path = settings.UPLOAD_TEMP_PATH + "/" + now_time +  file.name

        # Saving file to temp folder
        with open(temp_path, 'wb') as fp:
            fp.write(file.file.read())

        temp_file_hash = hash_file(temp_path)
        print(temp_file_hash)

        file_hash = ''
        try:
            file_hash = hash_file(path)
            print(file_hash)
        except:
            pass

        if file_hash == temp_file_hash:
            output['message'] = 'File with same content already uploaded'
            return Response(output)


        if os.path.isfile(path):
            output['message'] = 'File already uploaded'

        else:
            os.rename(temp_path, path)

            output['message'] = 'File uploaded'

        return Response(output)
        
    