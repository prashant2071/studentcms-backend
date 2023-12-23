from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True
    ""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Invalid email")
        # spacing haru hatauney
        email = self.normalize_email(email)  

        user = self.model(email=email, is_superuser=False, **extra_fields)
        user.set_password(password)
        user.save()