from django.db import models


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.name