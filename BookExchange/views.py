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
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import generics
from django.views import generic
from .models import Textbooks, Rating
from .serializers import TextbooksSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView

def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")
    
#this is the professor view
def professors(request):
    response= requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    return render(request,'professors.html',{'response':response})

class UserView(generic.ListView):
    model = User
    template_name = 'index.html'

class loginIndex(generic.ListView):
    model = Textbooks
    template_name = 'login.html'

class ProfileView(generic.ListView):
    model = Profile
    model = Rating
    template_name = 'userprofile.html'

def logout_view(request):
    logout(request)
    return redirect('login')

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
    
class ListTextbooksView(generics.ListAPIView):
    queryset = Textbooks.objects.all()
    serializer_class = TextbooksSerializer

def SellTextbooksList(request):
    
    # if request.method == 'POST':
    #     print("Posted")
    textbook_list = Textbooks.objects.all()
    return render(request, 'TextbooksList.html',{'textbook_list': textbook_list})

def SellTextbooksList(request):
    
    # if request.method == 'POST':
    #     print("Posted")
    textbook_list = Textbooks.objects.all()
    return render(request, 'TextbooksList.html',{'textbook_list': textbook_list})

def SellTextbooksView(request):
    response= requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    instructors = []
    courses = []

    for course in response:
        if (course["instructor"]["name"] not in instructors):
            if (course["instructor"]["name"] != "-"):
                instructors.append(course["instructor"]["name"])
        
        if (course["description"] not in courses):
            courses.append(course["description"])

    # print(instructors)

    return render(request,'SellTextbooks.html', {'instructors': sorted(instructors), 'courses': sorted(courses)})

class FavoritesView(generic.ListView):
    template_name = 'favorites.html'
    model = Textbooks

def SellTextbooksWrite(request):
    nameR = request.POST.get('name')
    authorR = request.POST.get('author')
    conditionR = request.POST.get('inCondition') 
    priceR = request.POST.get('price')
    instructor = request.POST.get('instructor')
    course = request.POST.get('course')
    isbn = request.POST.get('isbn')
    
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = "anonymous"
    test = Textbooks(name = nameR, author = authorR, condition = conditionR, price = priceR, creator = current_user, course = course, instructor = instructor, isbn = isbn)
    test.save()
    current_user.posts.add(test)
    return HttpResponseRedirect(reverse('textbooks-list'))

    # print(instructor, course)

def UpdateClassroom(request):
    name = request.POST.get('name')
    author = request.POST.get('author')
    condition = request.POST.get('condition') 
    price = request.POST.get('price')
    creator = request.POST.get('creator')
    current_user = request.user
    test = Textbooks.objects.get(name = name, author = author)
    #favorite = Textbooks.objects.get(pk=pk)
    if 'add_like' in request.POST:
        test.likes += 1
        current_user.favorites.add(test)

    # print(name)
    test.save()
    return HttpResponseRedirect(reverse('textbooks-list'))

def UpdateFavorites(request):
    name = request.POST.get('name')
    author = request.POST.get('author')
    condition = request.POST.get('condition') 
    price = request.POST.get('price')
    creator = request.POST.get('creator')
    current_user = request.user
    test = Textbooks.objects.get(name = name, author = author)
    current_user.favorites.remove(test)

    # print(name)
    test.save()
    return HttpResponseRedirect(reverse('favorites'))

class FilterView(generic.ListView):
    template_name = 'Filters.html'
    model = Textbooks

def ApplyFilters(request):
    qset = Textbooks.objects.all()
    nTitle = request.GET.get('inName')
    nAuthor = request.GET.get('inAuthor')
    nCondition = request.GET.get('inCondition')
    nPrice = request.GET.get('inPrice')
    nCourse = request.GET.get('course')
    nInstructor = request.GET.get('instructor')
    nIsbn= request.GET.get('inISBN')
    if nTitle  != '' and nTitle is not None:
        qset = qset.filter(name__icontains = nTitle)
    if nAuthor  != '' and nAuthor is not None:
        qset = qset.filter(author__icontains = nAuthor)
    if nCondition  != '' and nCondition is not None:
        qset = qset.filter(condition__icontains = nCondition)
    if nCourse  != '' and nCourse is not None:
        qset = qset.filter(course__icontains = nCourse)
    if nInstructor  != '' and nInstructor is not None:
        qset = qset.filter(instructor__icontains = nInstructor)
    if nIsbn  != '' and nIsbn is not None:
        qset = qset.filter(isbn__icontains = nIsbn)
    if nPrice == '0-50' and nPrice is not None:
        qset = qset.filter(price__range=(0,50))
    elif nPrice == '50.01-100' and nPrice is not None:
        qset = qset.filter(price__range=(50.01,100))
    elif nPrice == '100+' and nPrice is not None:
        qset = qset.filter(price__min=(100.01))
    adjusted = {
        'queryset': qset
    }
    return render(request, "AppliedFilters.html", adjusted)

def FiltersView(request):
    response= requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    instructors = []
    courses = []

    for course in response:
        if (course["instructor"]["name"] not in instructors):
            if (course["instructor"]["name"] != "-"):
                instructors.append(course["instructor"]["name"])
        
        if (course["description"] not in courses):
            courses.append(course["description"])

    # print(instructors)

    return render(request,'Filters.html', {'instructors': sorted(instructors), 'courses': sorted(courses)})

class UserProfileView(DetailView):
    model = User
    template_name = 'userprofile.html'
    select_related = ('profile',)

    def get_object(self):
        return self.get_queryset().get(username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context
