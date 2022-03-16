from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Dealer(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    company_name = models.CharField(max_length=100,verbose_name="Company's name")
    phone = models.CharField(max_length=15,verbose_name='Phone Number',null=True)
    additional_contact_info = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True,verbose_name='Address')
    description = models.TextField(max_length=500,null=True,verbose_name='Description')
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Create user')

    class Meta:
        verbose_name_plural = 'Dealer'

class Salesman(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    phone = models.CharField(max_length=12,verbose_name='Phone number')
    address = models.CharField(max_length=50,verbose_name='Address')
    email = models.CharField(max_length=100,null=True,verbose_name='E-mail')
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='dealer')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user',null=True)

    class Meta:
        verbose_name_plural = 'Salesman'

class Item(models.Model):
        name = models.CharField(max_length=100,null=True,verbose_name='Name')
        price = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='Price')
        description = models.TextField(max_length=500,null=True,verbose_name='Description')
        attribute = [('In stock','In stock'),('Out of stock','Out of stock')]
        status = models.CharField(max_length=12,choices=attribute,default='In stock',null=True,verbose_name='Status')
        dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='Dealer1')
        class Meta:
            verbose_name_plural = 'Item'

class Order(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name='Name')
    # unit = [('box','box'),('kilo','kilo'),('Pound','Pound')]
    quantity = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='Quantity')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date Ordered')
    salesman = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='salesman_orders',verbose_name='Salesman')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='item_orders')
    class Meta:
        verbose_name_plural ='Order'
