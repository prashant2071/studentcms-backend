from accounts.models import Profile
from rest_framework import serializers

class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        feilds = ['first_name','last_name','email']
        #fields = '__all__'
        exclude = [ 'password']