from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Dealer)
admin.site.register(Salesman)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(orderItems)