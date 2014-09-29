from django.db import models

# Create your models here.
class Content(models.Model):
    title_en = models.CharField(max_length=255)
    title_zh = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    update_date = models.CharField(max_length=255)
    count = models.CharField(max_length=255)