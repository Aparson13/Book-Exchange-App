from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('', include('mysite.urls')),
    path('mysite/', include('mysite.urls')),
    path('admin/', admin.site.urls),
]
