from django.db import models

class Photo(models.Model):
    header = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()

    def __str__(self):
        return self.description



class Title(models.Model):
    header = models.CharField(max_length=100)

    def __str__(self):
        return self.header
