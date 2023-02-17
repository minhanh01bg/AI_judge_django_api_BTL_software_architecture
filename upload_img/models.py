from django.db import models

# Create your models here.

# from django.contrib.auth.models import User


class Image(models.Model):
    Image = models.FileField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'