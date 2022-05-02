from django.shortcuts import render
from django.http import  HttpResponse 

# Create your views here.
def menu():
     return"""
             <a href="http://localhost:8000/Testapp/Hello/">Home</a>
             <a href="http://localhost:8000/Testapp/about/">About</a>
             <a href="http://localhost:8000/Testapp/contacts/">Contacts</a>
     """
def greeting (request):
    s="<h1>Welcome to my first Django Project</h1> Django is best platefrom of Web Development "
    s=menu()+s
    return HttpResponse(s)
def contacts (request):
    s="<h1>Welcome to context page<h1>"
    s=menu()+s
    return HttpResponse(s)
def about (request):
    s="<h1>Welcome to my About Page<h1>"
    s=menu()+s
    return HttpResponse(s)       