from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')


class SystemParametrs(models.Model):
    user = models.CharField(max_length=20, verbose_name='Имя пользователя')
    cpu = models.IntegerField(verbose_name='Загруженность CPU')

