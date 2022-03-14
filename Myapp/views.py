from django.shortcuts import render
from html5lib import serialize
from rest_framework import viewsets
from .serializers import DealerSerializer
from .models import Dealer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all().order_by('name')
    serializer_class = DealerSerializer