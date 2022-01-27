from django.db import models

# Create your models here.
class manoj(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)