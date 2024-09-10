from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Mensaje

def home(request):
    return render(request, 'mensajes/home.html')

def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario='Aira')  
    mensajes_enviados = Mensaje.objects.filter(remitente='Aira')  
    return render(request, 'mensajes/mensajes.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados
    })


def buscar_mensaje(request):
    if request.method == 'POST':
        query = request.POST.get('busqueda', '')
        mensajes = Mensaje.objects.filter(
            Q(remitente__icontains=query) | 
            Q(destinatario__icontains=query) | 
            Q(contenido__icontains=query)
        )
        return render(request, 'mensajes/buscar_mensajes.html', {'mensajes': mensajes, 'query': query})
    return render(request, 'mensajes/buscar_mensajes.html')


def eliminar_mensaje(request, mensaje_id):
    if request.method == 'POST':
        mensaje = get_object_or_404(Mensaje, id=mensaje_id)
        mensaje.delete()
        return redirect('ver_mensajes')
    return redirect('ver_mensajes')


def crear_mensaje(request):
    if request.method == 'POST':
        remitente = request.POST.get('remitente')
        destinatario = request.POST.get('destinatario')
        contenido = request.POST.get('contenido')
        Mensaje.objects.create(remitente=remitente, destinatario=destinatario, contenido=contenido)
        return redirect('ver_mensajes')
    return render(request, 'mensajes/crear_mensaje.html')
