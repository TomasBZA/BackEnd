from django import forms
from .models import Reserva
from django.core.exceptions import ValidationError

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if '@' not in correo:
            raise ValidationError('Ingrese un correo válido')
        return correo
    
    def clean_cantidad_personas(self):
        cantidad_personas = self.cleaned_data['cantidad_personas']
        if not 1 <= cantidad_personas <= 15:
            raise ValidationError('La cantidad de personas debe estar entre 1 y 15')
        return cantidad_personas
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) > 80:
            raise ValidationError('El nombre no puede superar los 80 caracteres')
        return nombre