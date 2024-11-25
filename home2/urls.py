from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Importar vistas genéricas de autenticación
from .views import (
    vista_home, vista_about, vista_funko, vista_contacto,
    vista_lista_producto, vista_agregar_producto, 
    vista_editar_producto, vista_ver_producto, vista_eliminar_producto,
    vista_configuracion, registro_usuario  # Agregar la vista de registro de usuario
)

urlpatterns = [
    # ----------- Páginas principales ----------- 
    path('', vista_home, name='home'),  # Página principal (Home)
    path('about/', vista_about, name='about'),  # Página "About"
    path('funko/', vista_funko, name='funko'),  # Página "Funko"
    path('contacto/', vista_contacto, name='contacto'),  # Página de contacto

    # ----------- Gestión de productos ----------- 
    path('lista_producto/', vista_lista_producto, name='lista_producto'),  # Listar productos
    path('agregar_producto/', vista_agregar_producto, name='agregar_producto'),  # Agregar producto
    path('editar_producto/<int:id_prod>/', vista_editar_producto, name='editar_producto'),  # Editar producto
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name='ver_producto'),  # Ver producto
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name='eliminar_producto'),  # Eliminar producto

    # ----------- Configuración ----------- 
    path('configuracion/', vista_configuracion, name='configuracion'),  # Configuración en JSON

    # ----------- Autenticación ----------- 
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Página de inicio de sesión
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Página de cierre de sesión
    path('registro/', registro_usuario, name='registro'),  # Página de registro de usuario
]
