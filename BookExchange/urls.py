from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('', include('myapp.urls')),
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
