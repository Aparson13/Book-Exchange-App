from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics
from .models import Textbooks
from .serializers import TextbooksSerializer


def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")

class ListTextbooksView(generics.ListAPIView):
    queryset = Textbooks.objects.all()
    serializer_class = TextbooksSerializer