from django.urls import path
from main.api_views import HomeView

urlpatterns=[
    path("",HomeView)
]