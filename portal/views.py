from django.http import HttpRequest, HttpResponse

def index(request):
    return HttpResponse("foo")