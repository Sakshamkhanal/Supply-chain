import re
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass 
    

class Dealer(models.Model):
  
    name = models.CharField(max_length=100,null=True)

    pan_no =  models.IntegerField(null=True,verbose_name='PAN number')

    email = models.CharField(max_length=200,null=True,verbose_name='Email')

    phn =  models.CharField(max_length=10,null=True,verbose_name='Phone')

    dsp = models.TextField(max_length=100,null=True,verbose_name='Description')

    crt_usr = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Create user')

    class Meta:
        verbose_name_plural = 'Dealer'

  

    
class Salesman(models.Model):
    null = models.TextField(max_length=100,null=True)

    var1= models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='SalesmanandDealer')

    var2 = models.OneToOneField(User,on_delete=models.CASCADE,related_name='salesmanandUser')
    class Meta:
        verbose_name_plural = 'Salesman'


class Items(models.Model):
    var3 = models.TextField(max_length=100,null=True)

    var4 = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='DealerandItems')

    class Meta:
        verbose_name_plural = 'Item'

class Order(models.Model):
    var5 = models.TextField(max_length=100,null=True)

    var6 = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='SalesmanOrder')

    var7 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='SalesmanItems')

    class Meta:
        verbose_name_plural = 'Order'


