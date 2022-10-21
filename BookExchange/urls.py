from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import ListTextbooksView

urlpatterns = [
   path('', TemplateView.as_view(template_name="index.html")),
   path('', views.index, name='index'), 
   path('accounts/', include('allauth.urls')),
   path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
   path('logout', LogoutView.as_view()),
   path('textbooks/', ListTextbooksView.as_view(), name="textbooks-all")
]
