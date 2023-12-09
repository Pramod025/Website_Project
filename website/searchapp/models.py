from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    mobile_number = models.CharField(max_length=10)
    colour = models.TextField()
    dob=models.DateField()