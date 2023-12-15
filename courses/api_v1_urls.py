from django.urls import path,include
from rest_framework import routers
from courses.viewsets import CourseViewSet


router = routers.DefaultRouter()
router.register(r'',CourseViewSet)

urlpatterns = [
    path('courses',include(router.urls))


]