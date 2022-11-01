from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import SellTextbooksView
from .views import SellTextbooksWrite
from .views import SellTextbooksList
from .views import ListTextbooksView
from .views import Profile



urlpatterns = [
   path('', TemplateView.as_view(template_name="index.html")),
   path('', views.index, name='index'), 
   path('accounts/', include('allauth.urls')),
   path('profile', views.Profilesv, name='profile'),
   #path('login', auth_view.LoginView.as_view(), name='login'),
   path('logout', LogoutView.as_view()),
   path('textbooks/', ListTextbooksView.as_view(), name="textbooks-all"),
   path('write/', SellTextbooksWrite, name="write-textbooks"),
   path('sell/', SellTextbooksView.as_view(), name="sell-textbooks"),
   path('list/', SellTextbooksList, name="textbooks-list"),
   path('professors/', views.professors, name = 'professors')
]
