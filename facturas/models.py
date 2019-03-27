from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField('nombre', max_length=45)
    precio = models.PositiveIntegerField('precio')
    cantidad = models.PositiveIntegerField('cantidad')
    total = models.PositiveIntegerField('total')

    def save(self, *args, **kwargs):
        self.total = self.precio * self.cantidad
        super(Producto, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        name = self.nombre+'-'+str(self.cantidad)
        return name


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=45)
    lugar = models.CharField('ciudad/Departamento', max_length=45)
    fecha = models.DateField('fecha')
    direccion = models.CharField('dirección', max_length=45)
    telefono = models.CharField('telefono', max_length=10)
    nit_cedula = models.IntegerField('cedula')
    productos = models.ManyToManyField(Producto, related_name="pedido")

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        name = self.nombre
        return name
