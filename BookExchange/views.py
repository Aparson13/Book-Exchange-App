from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from rest_framework import generics
from django.views import generic
from .models import Textbooks
from .serializers import TextbooksSerializer


def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")

class ListTextbooksView(generics.ListAPIView):
    queryset = Textbooks.objects.all()
    serializer_class = TextbooksSerializer

class SellTextbooksView(generic.ListView):
    template_name = 'SellTextbooks.html'
    model = Textbooks

def SellTextbooksWrite(request):
    nameR = request.POST.get('name')
    authorR = request.POST.get('author')
    conditionR = request.POST.get('condition')    
    test = Textbooks(name = nameR, author = authorR, condition = conditionR)
    test.save()
    return HttpResponseRedirect(reverse('textbooks-all'))