from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class UploadedImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

class Places(models.Model): 
    name = models.CharField(max_length = 30)
    image_url = models.CharField(max_length = 100)
    rgb = PickledObjectField()
    

