from datetime import date
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
   
    pan_no =  models.CharField(max_length=15,null=True,verbose_name='PAN number')


    email = models.CharField(max_length=200,null=True,verbose_name='Email')
    

    phn =  models.CharField(max_length=10,null=True,verbose_name='Phone')
    

    dsp = models.TextField(max_length=100,null=True,verbose_name='Description')
    

    crt_usr = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Create user',null=True)
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Dealer'

  

    
class Salesman(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name='Name')
    

    total_order=models.CharField(max_length=100,null=True,verbose_name='Total order')


    total_sales =models.CharField(max_length=100,null=True,verbose_name='Total sales')
    

    leftover = models.CharField(max_length=100,null=True,verbose_name='Remaining order')
    


    saso_dea= models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='sales_asso_dealer',null=True,verbose_name='salesman association with dealer') #saso_dea = salesman association with dealer


    saso_usr = models.OneToOneField(User,on_delete=models.CASCADE,related_name='sales_asso_user',null=True,verbose_name='salesman association with user') #saso_usr = salesman association with user

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Salesman'


class Items(models.Model):
    name= models.CharField(max_length=100,null=True,verbose_name='Name')
    

    price = models.CharField(max_length=100,null=True,verbose_name='Price')
    

    dsp = models.CharField(max_length=250,null=True,verbose_name='Description')
    

    stk_att =[('In stock','In stock'),('Out of stock','Out of stock')] #stk_att = stock attribute
   

    status = models.CharField(max_length=12,choices=stk_att,default='In stock',null=True)
    

    itm_dea = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='item_asso_dealer',null=True,verbose_name='Item association with Dealer') #item association with Dealer  

    def __str__(self):
        return self.name
   

    class Meta:
        verbose_name_plural = 'Item'

class Order(models.Model):
    Name = models.CharField(max_length=100,null=True)
   

    qty = {('box','box'),('kilo','kilo')}
    

    quanti = models.CharField(max_length=4,null=True,choices=qty,verbose_name='Quantity')

    date_crt = models.DateTimeField(auto_now_add=True,verbose_name="Date created")

    oaso_sal = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='order_asso_sales',null=True,verbose_name='Order association with sales')#Order association with sales
    

    iaso_sal = models.ForeignKey(Items,on_delete=models.CASCADE,related_name='items_asso_sales',null=True,verbose_name='Item association with sales')#Item association with sales

    def __str__(self):
        return self.Name
    

    class Meta:
        verbose_name_plural = 'Order'


