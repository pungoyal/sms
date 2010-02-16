from django.db import models

# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=1000)
    number = models.CharField(max_length=100)