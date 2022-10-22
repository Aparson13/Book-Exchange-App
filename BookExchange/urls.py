from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_view

#app_name = 'BookExchange'
urlpatterns = [
   path('', TemplateView.as_view(template_name="index.html")),
   path('', views.index, name='index'), 
   path('accounts/', include('allauth.urls')),
   path('profile', views.Profilesv, name='profile'),
   #path('login', auth_view.LoginView.as_view(), name='login'),
   path('logout', LogoutView.as_view()),
]
