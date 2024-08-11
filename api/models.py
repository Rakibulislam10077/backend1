from django.db import models

# Create your models here.

class student(models.Modal):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.name