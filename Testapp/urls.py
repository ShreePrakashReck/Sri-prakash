from django.urls import path
from .views import *
urlpatterns = [

   
    path('Hello/',greeting),
    path('contacts/',contacts),
    path('about/',about),
]
