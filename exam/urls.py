from django.urls import path
from .views import *
urlpatterns = [

    path('testPaper/', testPaper),
    path('exam/',testResult),
    
   
]
