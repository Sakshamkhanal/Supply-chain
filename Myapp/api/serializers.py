from dataclasses import field
import imp
from operator import mod
from pyexpat import model

from html5lib import serialize
from pyparsing import null_debug_action
from Myapp.models import *
from rest_framework import *

class DealerSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dealer
        fields = ('name','email','phone','description')

class SalesmanSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= Salesman
        fields = ('name','total_order','total_sales','leftover','dealer')

class ItemsSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Items
        fields = '__all__'

class OrderSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        field = '__all__'

