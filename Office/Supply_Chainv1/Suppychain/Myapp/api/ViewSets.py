from rest_framework import status
from django.shortcuts import get_object_or_404
from html5lib import serialize
from Myapp.api.serializers import DealerSerializer,SalesmanSerilizer,ItemSerilizer,OrderSerializer
from Myapp.models import Dealer,Item, Order,Salesman
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class DealerViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = DealerSerializer
    http_method_names = ['get', 'post', 'put',
                         'patch', 'head', 'options', 'trace']

    def get_queryset(self):
        # return today's list for shop of logged in user by default. filter by date if date parameter is provided.
        queryset = Dealer.objects.all()
        return queryset


    # def perform_create(self, serializer, *args, **kwargs):
    #     serializer.save(user=self.request.user,
    #                     shop=self.request.user.user_shop.shop)



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




################################################################################
################################################################################
# class SalesmanViewSet1(ModelViewSet):
#     def list(self,request,format=None):
#         salesman = Salesman.objects.all()
#         serializer = SalesmanViewSet(salesman)
#         return Response(serializer.data)
    
#     def create(self,request,format=None):
#         serializer = SalesmanSerilizer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self,request,pk,format=None):
#         salesman = get_object_or_404(Salesman.objects.all(),pk=pk)
#         salesman.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# ##################################################################################
# class ItemsViewSet1(ModelViewSet):
#     def list(self,request,format=None):
#         item = Item.objects.all()
#         serializer = ItemsViewSet(request.data)
#         return Response(serializer.data)

#     def create(self,request,format=None):
#         serializer = ItemsViewSet(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
 
#     def destroy(self,request,pk,format=None):
#         item = get_object_or_404(Item.objects.all(),pk=pk)
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class OrderViewset(ModelViewSet):
#     def list(self,request,format=None):
#         order = Order.objects.all()
#         serializer = OrderViewset(request.data)
#         return Response(serializer.data)

#     def create(self,request,format=None):
#         serializer = OrderViewset(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status= status.HTTP_201_CREATED)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self,request,pk,format=None):
#         order = Order.objects.all()
#         serializer = OrderViewset(request.data)
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class DealerViewSet1(ModelViewSet):
#     def list(self,request,format=None):
#         dealer = Dealer.objects.all()
#         serializer = DealerSerializer
#         return Response(serializer.data)
    
#     def create(self,request,format=None):
#         serializer = DealerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self,request,pk,format=None):
#         dealer = get_object_or_404(Dealer.objects.all(),pk=pk)
#         dealer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
