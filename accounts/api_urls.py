from django.urls import path
from accounts.api_view import StudentAPiView
from rest_framework import routers


urlpatterns = [
    path('',StudentAPiView),
    path('<int:id>', StudentAPiView),
    ]