from django.http import response
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse,JsonResponse

# Create your views here.
def hello (request):

    
    a={'q':'p'}
    #return HttpResponse("Http request is: "+str(request.get_host())  )
    return JsonResponse(a)