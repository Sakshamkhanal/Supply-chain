from posixpath import basename
from rest_framework import routers
from ViewSets import *
router = routers.SimpleRouter()
router.register('dealer',DealerViewSet,basename='dealer')
router.register('salesman',SalesmanViewSet,basename='salesman')
router.register('items',ItemsViewSet,basename='items')
router.register('order',OrderViewset,basename='order')