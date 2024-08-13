from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from accounts.manager import UserManager


class User(AbstractBaseUser):
    f_name = models.CharField(null=True, max_length=255)
    l_name = models.CharField(null=True, max_length=255)
    phone_number = models.CharField(unique=True, max_length=11)
    address = models.TextField(null=True)
    email = models.EmailField(unique=True, max_length=255)
    user_name = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = 'email'

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_modul_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

