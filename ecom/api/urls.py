from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.apiview, name='apiview'),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls')),
]