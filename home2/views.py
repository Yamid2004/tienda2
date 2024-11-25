from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import AgregarProductoForm, ContactoForm, RegistroUsuarioForm  # Importar formulario de registro de usuario
from .models import Producto
from .singleton import Configuracion  # Importar el Singleton
from django.contrib.auth.decorators import login_required  # Importar decorador para vistas protegidas
from django.contrib.auth import login  # Importar el método login de Django
from django.contrib.auth.forms import UserCreationForm  # Importar formulario de creación de usuario de Django


# Crear instancia global del Singleton para configuración
configuracion = Configuracion()
configuracion.agregar_configuracion('modo', 'producción')
configuracion.agregar_configuracion('version', '1.0.0')


# ----------- Vista para Configuración en JSON -----------

def vista_configuracion(request):
    """Vista para devolver configuración global en formato JSON"""
    datos = {
        "modo": configuracion.obtener_configuracion('modo'),
        "version": configuracion.obtener_configuracion('version'),
    }
    return JsonResponse(datos)


# ----------- Vista Lista de Productos -----------

@login_required
def vista_lista_producto(request):
    """Vista para listar todos los productos"""
    lista = Producto.objects.all()
    return render(request, 'lista_producto.html', {'lista': lista})


# ----------- Vista About -----------

def vista_about(request):
    """Vista de información 'About' usando el Singleton"""
    version = configuracion.obtener_configuracion('version')
    modo = configuracion.obtener_configuracion('modo')
    return render(request, 'about.html', {'version': version, 'modo': modo})


# ----------- Vista Funko -----------

def vista_funko(request):
    """Vista para la sección Funko (puede ser eliminada si ya no se usa)"""
    return render(request, 'funko.html')


# ----------- Vista Contacto -----------

def vista_contacto(request):
    """Vista para manejar un formulario de contacto"""
    info_enviado = False

    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            # Procesar datos del formulario si es necesario
            datos = formulario.cleaned_data
            print(f"Formulario enviado: {datos}")
    else:
        formulario = ContactoForm()

    return render(request, 'contacto.html', {
        'info_enviado': info_enviado,
        'formulario': formulario,
    })


# ----------- Vista Home -----------

def vista_home(request):
    """Vista para la página principal"""
    return render(request, 'home.html')


# ----------- Agregar Producto -----------

@login_required
def vista_agregar_producto(request):
    """Vista para agregar un producto nuevo"""
    if request.method == 'POST':
        formulario = AgregarProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_producto')
    else:
        formulario = AgregarProductoForm()

    return render(request, 'agregar_producto.html', {'formulario': formulario})


# ----------- Editar Producto -----------

@login_required
def vista_editar_producto(request, id_prod):
    """Vista para editar un producto existente"""
    producto = get_object_or_404(Producto, id=id_prod)

    if request.method == 'POST':
        formulario = AgregarProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_producto')
    else:
        formulario = AgregarProductoForm(instance=producto)

    return render(request, 'agregar_producto.html', {'formulario': formulario, 'producto': producto})


# ----------- Ver Producto -----------

def vista_ver_producto(request, id_prod):
    """Vista para ver detalles de un producto"""
    producto = get_object_or_404(Producto, id=id_prod)
    return render(request, 'ver_producto.html', {'producto': producto})


# ----------- Eliminar Producto -----------

@login_required
def vista_eliminar_producto(request, id_prod):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Producto, id=id_prod)
    producto.delete()
    return redirect('lista_producto')


# ----------- Registro de Usuario -----------

def registro_usuario(request):
    """Vista para registrar un nuevo usuario"""
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            # Crear el usuario y loguearlo automáticamente
            usuario = formulario.save()
            login(request, usuario)
            return redirect('home')  # Redirigir al inicio después de registrarse
    else:
        formulario = UserCreationForm()

    return render(request, 'registro.html', {'formulario': formulario})
