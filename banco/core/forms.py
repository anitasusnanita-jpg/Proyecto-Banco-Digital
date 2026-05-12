from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cuenta

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=False, label="Teléfono")
    foto_perfil = forms.ImageField(required=False, label="Foto de perfil")
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'foto_perfil', 'password1', 'password2')

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['numero_cuenta', 'tipos_cuenta']
        widgets = {
            'tipos_cuenta': forms.CheckboxSelectMultiple()
        }

class FormularioActualizarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'direccion', 'foto_perfil')