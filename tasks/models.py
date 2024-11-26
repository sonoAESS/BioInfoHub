from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)#se guarda la fecha y hora del momento de creacion
    datecompleted=models.DateTimeField(null=True, blank=True)#colocar fecha cuando cumplir, es opcional para administrador
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)#la idea es que cada usuario tenga su propia area de trabajo y si se borra el usuario se elimina el resto
    
    def __str__(self):
        return self.title  + '- by '+self.user.username