from rest_framework import routers
from django.urls import path,include
from Myapp.api.ViewSets import *

router = routers.DefaultRouter()
router.register(r'dealer',DealerViewSet,basename='dealer')
router.register(r'salesman',SalesmanViewSet,basename='salesman')
router.register(r'items',ItemsViewSet,basename='items')
router.register(r'order',OrderViewset,basename='order')
router.register(r'shop',ShopViewSet,basename='shop')

urlpatterns = [
    path('api/',include(router.urls)),
]
