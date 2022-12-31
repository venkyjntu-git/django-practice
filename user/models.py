from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    rollno=models.CharField(max_length=15,primary_key=True)
    marks=models.IntegerField()