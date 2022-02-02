from django.db import models


class Player(models.Model):
    name= models.CharField(max_length=90)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)