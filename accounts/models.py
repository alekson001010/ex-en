from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None,**kwargs):
        if not email:
            raise ValueError('Users must have an Email')

        user = self.model(
            email=email,**kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# ПОЛЬЗОВАТЕЛИ ---------------------------- проверить
class User(AbstractBaseUser,PermissionsMixin):
    gender_selection = [
        ('мужчина', 'мужчина'),
        ('женщина', 'женщина')
    ]
    goal = [
        ('decrease', 'decrease'),
        ('maintain', 'maintain'),
        ('increase', 'increase'),
    ]
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    last_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    date_subscribe = models.DateField(null=True, blank=True)
    days = models.IntegerField(default=0)
    initial_weight = models.IntegerField(null=True, blank=True, default=70)
    current_weight = models.IntegerField(null=True, blank=True, default=70)
    target_weight = models.IntegerField(null=True, blank=True, default=70)
    gender = models.CharField(choices=gender_selection, max_length=20, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    goal = models.CharField(choices=goal, max_length=20, null=True, blank=True)
    dailyCalories = models.IntegerField(default=0)

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'