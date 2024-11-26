from django.db import models

# Create your models here.
class Sequence(models.Model):
    file = models.FileField(upload_to='sequences/')
    result = models.TextField(blank=True)