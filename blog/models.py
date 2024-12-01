from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Item(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()

class Man(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    girlfriend = models.CharField(max_length=200, null=True, blank=True, verbose_name='Девушка')
    wife = models.BooleanField(default=False, verbose_name='Жена')

    def __str__(self):
        return self.surname