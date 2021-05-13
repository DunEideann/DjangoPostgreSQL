from django.db import models

# Create your models here.
class Todo(models.Model):
    user_id = models.IntegerField()
    do = models.TextField(max_length=200)
    privacy = models.BooleanField(default=True)

class Grid(models.Model):
    user_id = models.IntegerField()
    product = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    link = models.CharField(max_length=50, default="No link available")