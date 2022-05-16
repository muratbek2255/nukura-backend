from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Кастомная модель для пользователя"""
    username = models.CharField(max_length=150, default='Murat')
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class EcoCompany(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(CustomUser):
    image_company = models.CharField(max_length=1024, default='SII')
    description = models.TextField()
    phone_number = models.IntegerField(unique=False)
    eco_company = models.ForeignKey(to=EcoCompany, on_delete=models.SET_NULL, blank=True, null=True )
    address = models.CharField(max_length=100, default='Gogolya 123')

