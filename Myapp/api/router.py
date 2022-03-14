from Myapp.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('dealer',DealerViewSet,basename='Dealerview')

for url in router.urls:
    print(url,'\n')