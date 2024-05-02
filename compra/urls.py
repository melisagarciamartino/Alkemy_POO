from django.urls import path
from .views import (
    primera_vista,
    lista_productos, 
    productos_por_id,
    buscar_producto,
    ProductoCreateView, 
    ProductoUpdateView, 
    ProductoDeleteView,
    lista_proveedor, 
    proveedor_por_id,
    producto_proveedor,
    buscar_proveedor,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView
    )

app_name = "compra"

urlpatterns = [ 
               path("inicio/", primera_vista , name = "inicio"),
               path("productos/", lista_productos , name = "listado_productos"),
               path("producto_id/<int:id>/" , productos_por_id , name = "productos_por_id"),
               path("buscar_producto" , buscar_producto, name = "busqueda_producto"),
               path("crear_producto/", ProductoCreateView.as_view(), name= "producto_crear"),
               path("modificar_producto/<int:pk>", ProductoUpdateView.as_view(), name = "producto_modificar"),
               path("eliminar_producto/<int:pk>", ProductoDeleteView.as_view(), name = "producto_eliminar"),
               path("proveedores/", lista_proveedor , name = "listado_proveedores"),
               path("proveedor_id/<int:id>/" , proveedor_por_id , name = "proveedor_por_id"),
               path("buscar_proveedor" , buscar_proveedor, name = "busqueda_proveedor"),
               path("producto_proveedor/<int:id>/", producto_proveedor, name = "producto_proveedor"),
               path("crear_proveedor/", ProveedorCreateView.as_view(), name= "proveedor_crear"),
               path("modificar_proveedor/<int:pk>", ProveedorUpdateView.as_view(), name = "proveedor_modificar"),
               path("eliminar_proveedor/<int:pk>", ProveedorDeleteView.as_view(), name = "proveedor_eliminar"),
]