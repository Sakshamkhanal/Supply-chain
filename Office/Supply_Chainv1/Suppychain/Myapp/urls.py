from django.urls import path,include
from django.contrib import admin
from Myapp.api.router import router
 
 
urlpatterns =[
     path('api/',include(router.urls))
 ]
        