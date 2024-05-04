from django.contrib import admin
from .models import Producto,Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","precio","stock_actual","proveedor","foto"]
    fields = ["nombre","precio","stock_actual","proveedor","foto"]
    list_filter = ["nombre","precio","stock_actual","proveedor","foto"]
    ordering = ["nombre"]

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","apellido","dni","foto"]
    fields = ["nombre","apellido","dni","foto"]
    list_filter = ["nombre","apellido","dni","foto"]
    ordering = ["nombre"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)