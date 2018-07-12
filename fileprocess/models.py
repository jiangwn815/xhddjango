from django.db import models
from django.contrib.auth.models import User
import uuid
import os


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    sub_folder = 'file'
    folders = {
        "img": ['jpg', 'png', 'gif', 'jpeg', 'bmp'],
        "excel": ['csv', 'xls', 'xlsx'],
        "word": ['doc', 'docx'],
        "ppt": ['ppt', 'pptx']
    }
    for k, v in folders.items():
        if ext in v:
            sub_folder = k
    return os.path.join("user", str(instance.user.id), sub_folder, filename)


# Create your models here.
class imgSlide(models.Model):
    imgfile = models.ImageField(upload_to='imgslide')
    filename = models.CharField(max_length=64)


class UploadFile(models.Model):
    FILE_TYPES = (
        ('A', 'avatar'),
        ('E', 'excel'),
        ('W', 'word'),
        ('P', 'ppt'),
        ('O', 'Others')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filedata = models.FileField(upload_to=user_directory_path)
    filename = models.CharField(max_length=64)
    file_type = models.CharField(max_length=1, choices=FILE_TYPES)
