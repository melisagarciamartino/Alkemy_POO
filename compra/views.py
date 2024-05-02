from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Producto,Proveedor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

# Create your views here.

def primera_vista(request):
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "compra/inicio.html", {"productos" : productos,
                                                  "proveedores" : proveedores} )

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "compra/front_productos.html", {"productos" : productos})


#esto es para mostrar el producto al hacer click en id
def productos_por_id(request,id):
    productos = get_object_or_404(Producto, id=id)
    return render(request, "compra/productos_id.html" , {"productos": productos})

def buscar_producto(request):
    if request.method == 'POST':

       busqueda = request.POST.get('buscar')
       resultado_producto_nombre = Producto.objects.filter(nombre__contains = busqueda)
       return render(request,"compra/front_productos.html", {"productos" : resultado_producto_nombre})

    else:
        print("Producto no encontrado")

class ProductoCreateView(CreateView):
    model = Producto #clase que toma para crear objetos
    fields = ["nombre","precio","stock_actual","proveedor","foto"] #Esto es para saber que campos queremos mostrar del obejto
    template_name = "compra/producto_edit.html"
    success_url = "http://localhost:8000/compra/productos/"


class ProductoUpdateView(UpdateView):
    model = Producto #clase que toma para modificar objetos
    fields = ["nombre","precio","stock_actual","proveedor","foto"]#Esto es para saber que campos queremos mostrar del obejto
    template_name = "compra/producto_edit.html"
    success_url = "http://localhost:8000/compra/productos/"

class ProductoDeleteView(DeleteView):
    model = Producto 
    template_name = "compra/producto_eliminar.html"
    success_url = "http://localhost:8000/compra/productos/"


# Debajo se crea clase para poder Crear un proveedor, modificarlo, borrarlo y listarlo

def lista_proveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, "compra/front_proveedores.html", {"proveedores" : proveedor})

#esto es para mostrar el proveedor al dar click en nombre proveedor en listado productos y al hacer click en id cuando muestro los proveedores
def proveedor_por_id(request,id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, "compra/proveedor_id.html" , {"proveedores": proveedor})

def buscar_proveedor(request):
    if request.method == 'POST':

       busqueda = request.POST.get('buscar')
       resultado_producto_nombre = Proveedor.objects.filter(nombre__contains = busqueda)
       resultado_producto_apellido = Proveedor.objects.filter(apellido__contains = busqueda)
       return render(request,"compra/front_proveedores.html", {"proveedores" : resultado_producto_nombre,
                                                               "proveedores":resultado_producto_apellido})

    else:
        print("Producto no encontrado")

def producto_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    producto = proveedor.producto_set.all()
    return render(request, "compra/lista_productos_proveedor.html", {"lista_producto" : producto}) 

class ProveedorCreateView(CreateView):
    model = Proveedor 
    fields = ["nombre","apellido","dni","foto"] 
    template_name = "compra/proveedor_edit.html"
    success_url = "http://localhost:8000/compra/proveedores/"


class ProveedorUpdateView(UpdateView):
    model = Proveedor 
    fields = ["nombre","apellido","dni","foto"] 
    template_name = "compra/proveedor_edit.html"
    success_url = "http://localhost:8000/compra/proveedores/"

class ProveedorDeleteView(DeleteView):
    model = Proveedor 
    template_name = "compra/proveedor_eliminar.html"
    success_url = "http://localhost:8000/compra/proveedores/"