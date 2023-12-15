from rest_framework import viewsets
from accounts.models import Profile
from accounts.serializer import ProfileSerializer
 
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()