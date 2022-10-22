from cProfile import Profile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import UserManager, User, Profile, ProfileForms

def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")

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


# @verified_email_required()
# def home(request):
#     usuario = Perfil.objects.filter(user=request.user)
#     context = ({"usuario": usuario})
#     return render(request, "explore/inicioapp.html", context)

# @verified_email_required()
# def profile(request, id):
#     instance = get_object_or_404(Perfil, id=id)
#     form = ProfileForm(instance=instance)
#     if request.method == "POST":
#         form = ProfileForm(request.POST, instance=instance)
#         if form.is_valid():
#             perfil = form.save(commit=False)
#             perfil.user = request.user
#             perfil.save()
#             return HttpResponseRedirect("/profile/")
#     context = ({"form", form}, {"datos": instance})
#     return render(request, "explore/profile.html", context)