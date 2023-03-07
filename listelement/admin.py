from django.contrib import admin
from .models import Producto, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto')



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
