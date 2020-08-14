from django.db import models
class destination(models.Model):


    num = models.IntegerField()
    image=models.ImageField(upload_to='pics')
    img=models.ImageField(upload_to='pics')

    about=models.TextField()# Create your models here.
