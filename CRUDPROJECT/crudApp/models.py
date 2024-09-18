from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    message=models.CharField(max_length=400)
    Isdelete=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
