from django.urls import path

from rest_framework import routers
from .viewset import ProductoViewSet, CategoriaViewSet

route = routers.SimpleRouter()
route.register('Producto', ProductoViewSet)
route.register('Categoria', CategoriaViewSet)

 
urlpatterns = route.urls