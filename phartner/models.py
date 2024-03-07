from django.db import models


class MainTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Phartner(models.Model):
    image = models.ImageField(upload_to='phartner')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title



