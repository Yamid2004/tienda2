from django.shortcuts import redirect
from functools import wraps

def usuario_autenticado_requerido(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:  # Verifica si el usuario está autenticado
            return redirect('home')  # Redirige al inicio si no está autenticado
        return func(request, *args, **kwargs)
    return wrapper