from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=100)



class Employee(models.Model):
    image = models.ImageField(upload_to='employee_photos/')
    name = models.CharField(max_length=100)
    history = models.TextField()

    def __str__(self):
        return self.name




class GroupPhoto(models.Model):
    image = models.ImageField(upload_to='groupphotopy_photos/')
    description = models.TextField(default='')

    def __str__(self):
        return self.description