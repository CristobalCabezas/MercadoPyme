from rest_framework import viewsets
from rest_framework.response import Response
from .models import Producto, Categoria
from .serializer import ProductoSerializer, CategoriaSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Producto.objects.filter(category_id=pk)
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)