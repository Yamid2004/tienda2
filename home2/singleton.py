class SingletonMeta(type):
    """Una metaclase para implementar el patrón Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuracion(metaclass=SingletonMeta):
    """Clase de ejemplo que usa el patrón Singleton."""
    def __init__(self):
        self.config = {}

    def agregar_configuracion(self, clave, valor):
        self.config[clave] = valor

    def obtener_configuracion(self, clave):
        return self.config.get(clave, None)
