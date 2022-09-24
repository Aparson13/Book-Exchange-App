from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, B-22 Book Exchange is online.")