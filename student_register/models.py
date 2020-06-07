from django.db import models

# Create your models here.

class Roles(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Students(models.Model):
    fullname=models.CharField(max_length=100)
    sid=models.CharField(max_length=3)
    mobile=models.CharField(max_length=10)
    roles=models.ForeignKey(Roles,on_delete=models.CASCADE)