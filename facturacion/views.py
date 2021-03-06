from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, View
from facturas.models import Persona, Producto
from django.urls import reverse_lazy
from django import forms

# PDF
from facturacion.render import Render
from django.utils import timezone

# XML
import json
from django.core import serializers
from django.http import HttpResponse
from json2xml import json2xml


class HomeView(ListView):
    model = Persona
    template_name = "home.html"


class PersonDetail(DetailView):
    model = Persona
    template_name = "detailPerson.html"


class DeletePersona(DeleteView):
    model = Persona
    template_name = "ConfirmDeletelPerson.html"
    success_url = reverse_lazy('home')


class CreatePersona(CreateView):
    model = Persona
    fields = ['nombre', 'lugar', 'fecha', 'direccion',
              'telefono', 'nit_cedula', 'productos', 'correo']
    template_name = "createPerson.html"
    success_url = reverse_lazy('home')


class CreateProductos(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad']
    template_name = "createproduct.html"
    success_url = reverse_lazy('createPerson')


class Xml(View):
    def get(self, request, pk):
        person = Persona.objects.get(id=pk)
        today = timezone.now()
        products = person.productos.all()
        iva = 0.0
        total = 0
        subtotal = 0.0
        for product in products:
            iva += product.total*0.19
            total += product.total
        subtotal = total-iva
        params = {
            'fecha': person.fecha,
            'cliente': person.nombre,
            'lugar': person.lugar,
            'direccion': person.direccion,
            'telefono': person.telefono,
            'nit/cedula': person.nit_cedula,
            'correo': person.correo,
            'productos': products,
            'subtotal': subtotal,
            'iva': iva,
            'total': total
        }
        return HttpResponse(json2xml.Json2xml(params).to_xml(), content_type='aplication/xml')


class Pdf(View):
    def get(self, request, pk):
        person = Persona.objects.get(id=pk)
        today = timezone.now()
        products = person.productos.all()
        iva = 0.0
        total = 0
        subtotal = 0.0
        for product in products:
            iva += product.total*0.19
            total += product.total
        subtotal = total-iva
        params = {
            'request': request,
            'today': today,
            'persona': person,
            'products': products,
            'iva': iva,
            'subtotal': subtotal,
            'total': total

        }
        return Render.render('pdf.html', params)
