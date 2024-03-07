from django.db import models

class Blogs(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Stories(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Title(models.Model):
    header = models.CharField(max_length=100)

    def __str__(self):
        return self.header