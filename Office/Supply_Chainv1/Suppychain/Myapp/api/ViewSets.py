from rest_framework import status
from django.shortcuts import get_object_or_404
from html5lib import serialize
from Myapp.api.serializers import DealerSerializer,SalesmanSerilizer,ItemSerilizer
from Myapp.models import Dealer,Item, Order,Salesman
from rest_framework.response import Response
from rest_framework.views import APIView

class DealerViewSet(APIView):
    def get(self,request,format=None):
        dealer =Dealer.objects.all()
        serializer = DealerViewSet(dealer,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = DealerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        dealer = get_object_or_404(Dealer.objects.all(),pk=pk)
        dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SalesmanViewSet(APIView):
    def get(self,request,format=None):
        salesman = Salesman.objects.all()
        serializer = SalesmanViewSet(salesman,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = SalesmanSerilizer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        salesman = get_object_or_404(Salesman.objects.all(),pk=pk)
        salesman.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemsViewSet(APIView):
    def get(self,request,format=None):
        item = Item.objects.all()
        serializer = ItemsViewSet(request.data)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ItemsViewSet(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        item = get_object_or_404(Item.objects.all(),pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewset(APIView):
    def get(self,request,format=None):
        order = Order.objects.all()
        serializer = OrderViewset(request.data)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = OrderViewset(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        order = Order.objects.all()
        serializer = OrderViewset(request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)