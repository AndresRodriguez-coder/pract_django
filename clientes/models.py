from django.db import models

# Create your models here.
class clases (models.TextChoices):
    ALTA = 'Clase alta', 'Clase alta'
    MEDIA = 'clase media', 'clase media'
    BAJA = 'clase baja', 'clase baja'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()
    clase = models.TextField(choices=clases.choices, default=clases.BAJA)
    
    def __str__(self):
        return self.nombre
    