from sys import api_version
from rest_framework import status,permissions
from django.shortcuts import get_object_or_404
from html5lib import serialize
from Myapp.api.serializers import DealerSerializer,SalesmanSerilizer,ItemSerilizer,OrderSerializer, ShopSerializer
from Myapp.models import Dealer,Item, Order,Salesman, Shop
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from knox.auth import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer

class DealerViewSet(ModelViewSet):
    serializer_class = DealerSerializer
    http_method_names = ['get', 'post', 'put',
                         'patch', 'head', 'options', 'trace']

    def get_queryset(self):
        queryset = Dealer.objects.all()
        return queryset


class SalesmanViewSet(ModelViewSet):
    serializer_class = SalesmanSerilizer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set = Salesman.objects.all()
        return query_set

class ItemsViewSet(ModelViewSet):
    serializer_class = ItemSerilizer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set =  Item.objects.all()
        return query_set
        
class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set = Order.objects.all()
        return query_set


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']
    
    def get_queryset(self):
        query_set = Shop.objects.all()
        return query_set

