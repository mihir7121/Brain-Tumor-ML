from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title