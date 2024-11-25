# proxies.py
from .models import Producto

class ProductoProxy:
    def __init__(self, producto_id):
        self.producto_id = producto_id
        self._producto = None  # El objeto real de Producto se carga de forma perezosa

    def _cargar_producto(self):
        if self._producto is None:
            self._producto = Producto.objects.get(id=self.producto_id)
        return self._producto

    def obtener_precio(self):
        producto = self._cargar_producto()
        return producto.precio

    def obtener_nombre(self):
        producto = self._cargar_producto()
        return producto.nombre

    def obtener_descripcion(self):
        producto = self._cargar_producto()
        return producto.descripcion
