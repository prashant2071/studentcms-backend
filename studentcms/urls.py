"""
URL configuration for studentcms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main.views import HomeView,getToken
# from accounts.views import StudentView,AddStudents
from courses.views import StudentCourses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='home'),
    
    path('students/',include('accounts.urls')),
    path('courses/',include('courses.urls')),

# for api
    path('api/token/',getToken),
    path('api/',include('main.api_urls')),
    path('api/students/',include('accounts.api_urls')),
    path('api/courses/',include('courses.api_urls')),

# for api_v1
    path('api/v1/students/',include('accounts.api_v1_urls')),
    path('api/v1/courses/',include('courses.api_v1_urls')),

]
