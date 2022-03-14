from crypt import methods
from html5lib import serialize
from Myapp.models import Dealer
from Myapp.api.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
class DealerViewSet(viewsets.ViewSet):

    def list(self,request):
        queryset = Dealer.objects.all()
        serializer = DealerSerializers(queryset,many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def newest(self,request):
        newest = self.get_query_set().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
 

class SalesmanViewSet(viewsets.ViewSet):
        def list(self,request):
            queryset = Salesman.objects.all()
            serializer = SalesmanSerializers(queryset,many=True)
            return Response(serializer.data)







# class MyappViewSet(viewsets.ModelViewSet):
#     queryset = Dealer.objects.all()
# list,create,retrive,update,partial_update, destroy
#     serializer_class = MyappSerializers