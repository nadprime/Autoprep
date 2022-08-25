import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name

class FileModel(models.Model):
   file = models.FileField(upload_to="file/")

class ImageModel(models.Model):
    file = models.ImageField(upload_to="img/")