from django.db import models

# Create your models here.
from django.db import models

class Uno(models.Model):
    UnoId=models.AutoField(primary_key=True)
    username =models.CharField(max_length=100 ,blank=False,null=False )
    password=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.username