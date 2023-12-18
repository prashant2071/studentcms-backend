from django.urls import path,include
from rest_framework import routers
from courses.viewsets import CourseViewSet,StudentCourseViewSet


router = routers.DefaultRouter()
router.register(r'',CourseViewSet)

router1 = routers.DefaultRouter()
router1.register(r'',StudentCourseViewSet)

urlpatterns = [
    path('courses/',include(router.urls)),
    path('studentcourses/',include(router1.urls))
    



]