from cProfile import Profile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import UserManager, User, Profile, ProfileForms
from django.shortcuts import render
import requests
from django.urls import reverse

from rest_framework import generics
from django.views import generic
from .models import Textbooks
from .serializers import TextbooksSerializer

def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")
    
#this is the professor view
def professors(request):
    response= requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    return render(request,'professors.html',{'response':response})

class UserView(generic.ListView):
    model = User
    template_name = 'index.html'

class ProfileView(generic.ListView):
    model = Profile
    template_name = 'profile.html'
    

def Profilesv(request):
    if request.method == 'POST':
        form = ProfileForms(request.POST)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = request.user
            profile.last_name = form.cleaned_data.get('last_name')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.major = form.cleaned_data.get('major')
            profile.location = form.cleaned_data.get('location')
            profile.year = form.cleaned_data.get('year')
            profile.save()
            return render(request, 'BookExchange/profile.html', {'form': form})
    else:
        form = ProfileForms()
    return render(request, 'BookExchange/profile.html', {'form': form})
    
#class ListTextbooksView(generics.ListAPIView):
    #queryset = Textbooks.objects.all()
    #serializer_class = TextbooksSerializer

def deepthoughtsList(request):
    deepthought_list = deepthought.objects.all()
    return render(request, 'polls/deepthoughtsList.html',{'deepthought_list': deepthought_list})

class SellTextbooksView(generic.ListView):
    template_name = 'SellTextbooks.html'
    model = Textbooks

def SellTextbooksWrite(request):
    nameR = request.POST.get('name')
    authorR = request.POST.get('author')
    conditionR = request.POST.get('condition') 
    priceR = request.POST.get('price')
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = "anonymous"
    test = Textbooks(name = nameR, author = authorR, condition = conditionR, price = priceR, creator = current_user)
    test.save()
    return HttpResponseRedirect(reverse('textbooks-all'))

