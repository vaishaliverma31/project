from django.db import models

# Create your models here.
class studentdetail(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    
