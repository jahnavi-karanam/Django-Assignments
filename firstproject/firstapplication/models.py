from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=15)
    Id=models.IntegerField()
    Contact_email=models.EmailField(max_length=15)
    Address=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.Name
