from dataclasses import field
from pyexpat import model
from threading import activeCount
from rest_framework import serializers
from Myapp.models import *

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        field ="__all__"
    def create(self,validate_data):
        return Dealer(**validate_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.company_name = validated_data.get("Company's name",instance.company_name)
        instance.phone = validated_data.get('Phone Number',instance.phone)
        instance.additional_contact_info = validated_data.get('additional_contact_info',instance.additional_contact_info)
        instance.description = validated_data.get('address',instance.description)
        instance.user = validated_data.get('user',instance.user)

class SalesmanSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        field = "__all__"
        def create(self,validated_data):
            return Salesman(**validated_data)

        def update(self,instance,validated_data):
            instance.name = validated_data.get('name',instance.name)
            instance.phone = validated_data.get('phone',instance.phone)
            instance.address = validated_data.get('address',instance.address)
            instance.email = validated_data.get('email',instance.email)
            instance.dealer = validated_data.get('dealer',instance.dealer)
            instance.user = validated_data.get('user',instance.user)


class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = "__all__"
        def create(self,validated_data):
            return Item(**validated_data)

        def update(self,instance,validated_data):
            instance.name = validated_data.get('name',instance.name)
            instance.price = validated_data.get('phone',instance.price)
            instance.description = validated_data.get('address',instance.description)
            instance.email = validated_data.get('email',instance.email)
            instance.dealer = validated_data.get('dealer',instance.dealer)
            instance.user = validated_data.get('user',instance.user)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = "__all__"
        def create(self,validated_data):
            return Item(**validated_data)

        def update(self,instance,validated_data):
            instance.name = validated_data.get('name',instance.name)
            instance.quantity = validated_data.get('quantity',instance.quantity)
            instance.salesman = validated_data.get('salesman',instance.salesman)
            instance.item = validated_data.get('dealer',instance.item)
            