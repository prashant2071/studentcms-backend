from django.urls import path,include
from rest_framework import routers
from accounts.viewsets import ProfileViewSet


router = routers.DefaultRouter()
router.register(r'',ProfileViewSet,basename='profile')



urlpatterns = [    
    path('',include(router.urls)),

]