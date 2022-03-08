from pyexpat import model
import re
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from more_itertools import quantify


# Create your models here.
class User(AbstractUser):
    pass 
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=10)

class Dealer(models.Model):
  
    name = models.CharField(max_length=100,null=True)
    print('here1')

    pan_no =  models.CharField(max_length=15,null=True,verbose_name='PAN number')
    print('here2')

    email = models.CharField(max_length=200,null=True,verbose_name='Email')
    print('here3')

    phn =  models.CharField(max_length=10,null=True,verbose_name='Phone')
    print('here4')

    dsp = models.TextField(max_length=100,null=True,verbose_name='Description')
    print('here5')

    crt_usr = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Create user',null=True)
    print('here6')

    class Meta:
        verbose_name_plural = 'Dealer'

  

    
class Salesman(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name='Name')
    print('here7')

    total_order=models.CharField(max_length=100,null=True,verbose_name='Total order')
    print('here8')

    total_sales =models.CharField(max_length=100,null=True,verbose_name='Total sales')
    print('here9')

    leftover = models.CharField(max_length=100,null=True,verbose_name='Remaining order')
    print('here10')


    saso_dea= models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='sales_asso_dealer',null=True) #saso_dea = salesman association with dealer
    print('here11')

    saso_usr = models.OneToOneField(User,on_delete=models.CASCADE,related_name='sales_asso_user',null=True) #saso_usr = salesman association with user
    print('here12')

    class Meta:
        verbose_name_plural = 'Salesman'


class Items(models.Model):
    name= models.CharField(max_length=100,null=True,verbose_name='Name')
    print('here13')

    price = models.CharField(max_length=100,null=True,verbose_name='Price')
    print('here14')

    dsp = models.CharField(max_length=250,null=True,verbose_name='Description')
    print('here15')

    stk_att =[('In stock','In stock'),('Out of stock','Out of stock')] #stk_att = stock attribute
    print('here16')

    status = models.CharField(max_length=12,choices=stk_att,default='In stock',null=True)
    print('here17')

    itm_dea = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='item_asso_dealer',null=True) #item association with Dealer  
    print('here18')

    class Meta:
        verbose_name_plural = 'Item'

class Order(models.Model):
    Name = models.CharField(max_length=100,null=True)
    print('here19')

    qty = {('box','box'),('kilo','kilo')}
    print('here20')

    quanti = models.CharField(max_length=4,null=True,choices=qty,verbose_name='Quantity')
    print('here21')

    oaso_sal = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='order_asso_sales',null=True)#Order association with sales
    print('here22')

    iaso_sal = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='items_asso_sales',null=True)#Item association with sales
    print('here23')

    class Meta:
        verbose_name_plural = 'Order'


