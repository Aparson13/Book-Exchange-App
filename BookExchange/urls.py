from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import SellTextbooksView
from .views import SellTextbooksWrite
from .views import SellTextbooksList, ApplyFilters
from .views import ListTextbooksView, logout_view
from .views import Profile, ProfileView, FilterView



urlpatterns = [
   path('', TemplateView.as_view(template_name="index.html")),
   path('', views.index, name='index'), 
   path('accounts/', include('allauth.urls')),
   path('profile', views.Profilesv, name='profile'),
   #path('login', auth_view.LoginView.as_view(), name='login'),
   path('logout', logout_view, name="logout"),
   path('textbooks/', ListTextbooksView.as_view(), name="textbooks-all"),
   path('filter/', FilterView.as_view(), name="filter"),   
   path('applyFilter/', ApplyFilters, name="applyFilters"),
   path('write/', SellTextbooksWrite, name="write-textbooks"),
   path('sell/', SellTextbooksView.as_view(), name="sell-textbooks"),
   path('list/', SellTextbooksList, name="textbooks-list"),
   path('professors/', views.professors, name = 'professors'),
   path('userprofile', ProfileView.as_view(template_name='userprofile.html'))

]
