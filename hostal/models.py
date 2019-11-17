from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    run = models.CharField('Rut',max_length=12,null=True)
    empresa = models.CharField('Nombre Empresa', max_length=100, null= True)
    cargo = models.CharField('Cargo Empresa', max_length=100, null= True)
    direccion = models.CharField('Direccion', max_length=100, null= True)
    telefono = models.CharField('Telefono', max_length=100, null= True)
    ciudad = models.CharField('Ciudad',max_length=50,null=True)

    def publish(self):
        self.save()
    

    def __str__(self):
     return self.user.email


@receiver(post_save, sender=User)
def update_user_cliente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)
    instance.cliente.save()


class Comedor(models.Model):

    nombre = models.CharField('Nombre Menu', max_length=100, null= True)
    fecha = models.DateField('Fecha', null=True)
    entrada = models.CharField('Entrada', max_length=100, null= True)
    plato = models.CharField('Plato Principal', max_length=100, null= True)
    postre = models.CharField('Postre', max_length=100, null= True)
    precio=models.IntegerField('Precio Menu',null= True)

    def __str__(self):
     return self.nombre


class Comedor2(models.Model):

    nombreplato = models.CharField('Nombre Plato', max_length=100, null= True)
    descripcion = models.CharField('Plato Descripcion', max_length=100, null= True)
    precio=models.IntegerField('Precio Plato',null= True)
    servicio = models.CharField('Servicio', max_length=100, null= True)

    def __str__(self):
     return self.nombreplato









