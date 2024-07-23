from django.db import models

class student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    image = models.ImageField()
    file = models.FileField()

class car(models.Model):
    car_name=models.CharField(max_length=100)
    top_speed=models.IntegerField(default=50)
    def __str__(self) -> str:
        return self.car_name