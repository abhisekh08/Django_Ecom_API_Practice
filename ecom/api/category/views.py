from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class  = CategorySerializer