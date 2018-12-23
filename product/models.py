from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to='images')
    icon=models.ImageField(upload_to='images')
    votes=models.IntegerField(default=0)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)