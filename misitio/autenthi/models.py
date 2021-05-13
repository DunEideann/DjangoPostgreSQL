from django.db import models

# Create your models here.
class Users(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.TextField(max_length=30)


