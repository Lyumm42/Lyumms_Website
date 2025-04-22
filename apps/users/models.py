from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):

    first_name = None
    last_name = None

    email = models.EmailField( "Электронная почта",max_length=225, unique=True)
    address = models.CharField("Адрес", max_length=100, null=True, blank=True)
    mobile = models.CharField("Телефон", max_length=15, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='default/avatar.png')


    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()