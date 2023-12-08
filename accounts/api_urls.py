from django.urls import path
from accounts.api_view import StudentAPiView

urlpatterns = [
    path('',StudentAPiView),
    path('<int:id>', StudentAPiView),
]