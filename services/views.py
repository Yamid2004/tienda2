from home2.models import *
from .serializer import *
from rest_framework import viewsets

class producto_viewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer

# patron de MVC gestionando la interaccion enttre usuario y el sistema y asistiendo la logica al acceso a datos a los controladores

# patron VieWset facilita las operaciones CRUD sin necesidad de escribir mucho codigo.

#patron de Query permite la consulta a la base de datos y permite la reutulzacion y mantenimiento de las consultas.