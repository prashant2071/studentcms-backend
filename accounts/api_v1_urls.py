from django.urls import path,include,re_path
from rest_framework import routers
from accounts.viewsets import ProfileViewSet,FileUploadView


router = routers.DefaultRouter()
router.register(r'',ProfileViewSet,basename='profile')



urlpatterns = [
    re_path(r'upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('', include(router.urls)),
]
