from django.db import models

class What_We_Do(models.Model):
    image = models.ImageField(upload_to='photos/', default='default_image.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title