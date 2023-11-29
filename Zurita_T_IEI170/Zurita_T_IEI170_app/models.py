from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

# Create your models here.
class Reserva(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )
    nombre = models.CharField(max_length=80, validators=[MaxLengthValidator(80)])
    telefono = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo = models.EmailField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)