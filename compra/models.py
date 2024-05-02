from django.db import models
from django.urls import reverse

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    foto = models.ImageField(upload_to='proveedor_img/', default= 'contacto.png')

    def __str__(self):
        return F"{self.nombre} {self.apellido}"
    
    def get_absolute_url(self):

       return reverse("compra:proveedor_por_id" , kwargs = {"id": self.id})


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField() or models.IntegerField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete= models.CASCADE, null=True , blank=True)
    foto = models.ImageField(upload_to='producto_img/', default= 'producto_default.avif')
    

    def __str__(self):
        return F"{self.nombre.upper()}"
    
    def get_absolute_url(self):

       return reverse("compra:productos_por_id" , kwargs = {"id": self.id})
    
       


