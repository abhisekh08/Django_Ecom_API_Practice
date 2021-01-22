from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apiview(request):
    return HttpResponse(JsonResponse({'name': "abhisekh",'work':'coder'}))

