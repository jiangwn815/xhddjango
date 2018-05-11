from django.db import models

# Create your models here.
class imgSlide(models.Model):
    imgfile = models.ImageField(upload_to='imgslide')
    filename = models.CharField(max_length=64)