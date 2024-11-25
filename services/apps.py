from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

#patron de singleton asegurando que solo haya una sola instancia de la configuracion en la aplicacion

# patron configuracion centraliza la definicion de la configuracion de la app para que sea facilmente accesible y modificable. 
