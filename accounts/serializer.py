from accounts.models import Profile
from rest_framework import serializers,validators

# class ProfileSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         feilds = ['first_name','last_name','email']
#         #fields = '__all__'
#         exclude = [ 'password']

class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    
class ProfileDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['password']

class ProfileCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length = 10,min_length=3)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(
        validators = [
            validators.UniqueValidator(queryset = Profile.objects.all())
        ]
    )
    password = serializers.CharField(required = True)
    phone = serializers.CharField(required = False )
    
class ProfilePatchSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 10,min_length=3 ,required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(
         required = False,
         validators = [
             validators.UniqueValidator(queryset=Profile.objects.all())
         ]
     )
    password = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)