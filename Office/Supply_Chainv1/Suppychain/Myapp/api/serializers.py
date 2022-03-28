from dataclasses import field
from pyexpat import model
from threading import activeCount
from rest_framework import serializers
from Myapp.models import *

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ("__all__")
class SalesmanSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = ("__all__")

class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("__all__")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = "__all__"

            
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        field ="__all__"