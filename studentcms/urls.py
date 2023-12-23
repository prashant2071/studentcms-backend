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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="StudentCMS API",
      default_version='v1',
      description="StudentCMS API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ab@gmail.com"),
      license=openapi.License(name="GNU License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(),
)
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
    path('api/v1/',include('userauth.urls')),
# swagger
path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
