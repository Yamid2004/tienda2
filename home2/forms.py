from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

# Formulario para agregar un producto
class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['status']

    # Cambiar la marca para que sea un campo de texto
    marca = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Marca del Producto",
        max_length=100
    )


# Formulario para la sección de contacto
class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
        label="Nombre"
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo'}),
        label="Correo Electrónico"
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tu mensaje'}),
        label="Mensaje"
    )


# Formulario para registrar un nuevo usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Puedes agregar validaciones personalizadas aquí si lo deseas
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
