from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    nombre_categoria = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255, null= True)
    
   
    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    
    
    nombre_producto = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255, null=True)
    marca= models.CharField(max_length=255, null=True)
    proveedor = models.CharField(max_length=255, null=True)
    descripcion = models.TextField(null=True)
    precio_producto = models.IntegerField(null=True)
    codigo_producto = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
    


    

