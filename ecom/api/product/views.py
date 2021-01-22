from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer