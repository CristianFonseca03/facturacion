from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView
from facturas.models import Persona, Producto
from django.urls import reverse_lazy
from django import forms

# PDF
from django.http import HttpResponse
from reportlab.pdfgen import canvas


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
    fields = ['nombre', 'precio', 'iva_aplicable', 'cantidad']
    template_name = "createproduct.html"
    success_url = reverse_lazy('createPerson')
