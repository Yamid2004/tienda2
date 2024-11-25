from django.urls import path, include
from rest_framework import routers
from home2.models import *
from services.views import *

router = routers.DefaultRouter()
router.register(r'productos', producto_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


#patron de RESTful organiza los recursos productos - marca - categoria en rutas logicas 

#patron de router gestiona de manera automatica la asignacion de urls a las vistas.