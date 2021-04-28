from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import *
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Pastel(models.Model):
    usuarios = models.ManyToManyField(User)
    
    status_pastel = models.BooleanField(blank=True)
    
    class Formas(models.TextChoices):
        Circular = 'CI', _('Circular')
        Cuadrado = 'CU', _('Cuadrado')

    forma = models.TextField(choices=Formas.choices)

    num_pisos = models.IntegerField(blank=True)
    
    porciones = models.IntegerField(blank=True)

    class Masas(models.TextChoices):
        Vainilla = 'VA', _('Vainilla')
        Chocolate = 'CH', _('Chocolate')
        Tres_Leches = 'TL', _('Tres Leches')
        Red_Velvet = 'RV', _('RedVelvet')

    masa = models.CharField(
        choices=Masas.choices,
        max_length=2
    )

    class Rellenos(models.TextChoices):
        Arequipe = 'AQ', _('Arequipe')
        Nutella = 'NU', _('Nutella')
        Mermelada = 'ML', _('Mermelada') 
        Crema_Pastelera = 'CP', _('CremaPastelera')

    relleno = models.CharField(
        choices=Rellenos.choices,
        max_length=2
    )

    class Cobertura(models.TextChoices):
        Crema = 'CR', _('Crema')
        Fondant = 'FD', _('Fondant')

    Cobertrura = models.CharField(
        choices=Cobertura.choices,
        max_length=2
    )
    class ColorCobertura(models.TextChoices):
        Azul = 'CR', _('Crema')
        Fondant = 'FD', _('Fondant')

    Cobertrura = models.CharField(
        choices=Cobertura.choices,
        max_length=2
    )

    costo = models.FloatField(blank=False, default=0)
    

class Pedido(models.Model):
    pasteles = models.ManyToManyField(Pastel)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    costo = models.FloatField(blank=True) 
    status = models.BooleanField(blank=True)
    correo_asociado = models.EmailField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length =255)
