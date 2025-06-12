from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
