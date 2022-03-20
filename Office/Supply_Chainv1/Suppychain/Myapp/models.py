from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Dealer(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
    company_name = models.CharField(max_length=100,verbose_name="Company's name",null=True,blank=True)
    phone = models.CharField(max_length=15,verbose_name='Phone Number',null=True,blank=True)
    additional_contact_info = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,verbose_name='Address',null=True,blank=True)
    description = models.TextField(max_length=500,verbose_name='Description',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Dealer'
class Salesman(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
    phone = models.CharField(max_length=12,verbose_name='Phone number',null=True,blank=True)
    address = models.CharField(max_length=50,verbose_name='Address',null=True,blank=True)
    email = models.CharField(max_length=100,verbose_name='E-mail',null=True,blank=True)
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='dealer')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')

    class Meta:
        verbose_name_plural = 'Salesman'

class Item(models.Model):
        name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
        price = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='Price',null=True,blank=True)
        description = models.TextField(max_length=500,verbose_name='Description',null=True,blank=True)
        attribute = [('In stock','In stock'),('Out of stock','Out of stock')]
        status = models.CharField(max_length=12,choices=attribute,default='In stock',verbose_name='Status',null=True,blank=True)
        dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='Dealer1')
        class Meta:
            verbose_name_plural = 'Item'
        
        def __str__(self):
            return self.name

class Order(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name='Name')
    # unit = [('box','box'),('kilo','kilo'),('Pound','Pound')]
    quantity = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='Quantity')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date Ordered')
    salesman = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='salesman_orders',verbose_name='Salesman')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='item_orders')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural ='Order'
