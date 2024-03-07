from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title



class Mission(models.Model):
    headers = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.headers


class Activities(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.header


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.image.name


class lists(models.Model):
    home = models.CharField(max_length=100)
    social = models.CharField(max_length=100)
    gallery = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    done = models.CharField(max_length=100)
    doing = models.CharField(max_length=100)
    partnership = models.CharField(max_length=100)
    apps = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    meniu = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.home


class Contact(models.Model):  # Changed to start with uppercase
    image = models.ImageField(upload_to='photos/')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.city
