from rest_framework import serializers
from home2.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'nombre', 'descripcion', 'status', 'foto', 'precio', 'stock', 'marca', 'categorias')

class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'id', 'nombre')

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url','nombre')


#patron MVC modelo-vista-controlador se basa en la estructura de datos y interactuar con la based de datos.

#patron de diseño serializers que basicamente cambia el modelo de datos a formato json.