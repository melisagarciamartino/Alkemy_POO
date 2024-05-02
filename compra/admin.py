from django.contrib import admin
from .models import Producto,Proveedor

# Register your models here.

#admin.site.register(Producto)
#admin.site.register(Proveedor)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","stock_actual","proveedor","foto"]
    fields = ["nombre","precio","stock_actual","proveedor","foto"]
    list_filter = ["nombre","precio","stock_actual","proveedor","foto"]
    ordering = ["nombre"]

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","dni","foto"]
    fields = ["nombre","apellido","dni","foto"]
    list_filter = ["nombre","apellido","dni"]
    ordering = ["nombre"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)