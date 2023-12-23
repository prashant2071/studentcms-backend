from django.db import models
from userauth.manager import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=False)
    is_staff = models.BooleanField(('active'),default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # here user manager act as basemodel which has extra fields like 
    objects =  UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    
    # REQUIRED_FIELDS = ['email']
    