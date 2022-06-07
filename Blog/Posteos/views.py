
from msilib.schema import ListView
from pathlib import PosixPath
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django import http
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from Posteos.models import Post, Profesor, Avatar
from Posteos.forms import UserRegistrationForm, UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


@login_required
def home(request):
    avatar=Avatar.objects.filter(user=request.user)
    return render(request,'Posteos/home.html',{'url': avatar[0].avatar.url})

def AcercaDeMi(request):
    return render(request,'Posteos/about.html')

def comodin(request):
    return render(request,'Posteos/comodin.html')


def req_login(request):
    if request.method=='POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,'Posteos/home.html',{'usuario':usuario, 'mensaje':'Bienvenido nuevamente.'})
            else:
                return render(request,'Posteos/login.html',{'formulario':formulario,'mensaje':'Datos incorrectos. Vuelva a intentar.'})
        else:
            return render(request,'Posteos/login.html',{'formulario':formulario,'mensaje':'Datos inválidos. Vuelva a intentar.'})
    else:
        formulario=AuthenticationForm()
        return render(request, 'Posteos/login.html', {'formulario':formulario})

def register(request):
    if request.method=='POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request,'Posteos/home.html',{'mensaje':f'Usuario: {username} creado con éxito.'})
        else:
            return render(request,'Posteos/home.html',{'mensaje':'No se pudo crear el usuario.'})
    else:
        formulario = UserRegistrationForm()
        return render(request,'Posteos/register.html',{'formulario':formulario})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=='POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request,'Posteos/home.html',{'usuario':usuario,'mensaje':'Se ha editado exitosamente el perfil.'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request,'Posteos/editarperfil.html', {'formulario':formulario, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method=='POST':
        formulario=AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)

            if(avatarViejo.avatar):
                avatarViejo.delete()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()

            return render(request, 'Posteos/home.html',{'usuario':user, 'mensaje':'Imagen guardada.'})
    else:
        formulario=AvatarForm()
    return render(request, 'Posteos/agregarElAvatar.html',{'formulario':formulario,'usuario':user})

@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
        
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()
        
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'Posteos/home.html', {'usuario':user, 'mensaje':'Imagen guardada'})
    else:
        formulario=AvatarForm()
    return render(request, 'Posteos/agregarElAvatar.html', {'formulario':formulario, 'usuario':user})


#Posteos -------------------------------

class PosteoList(LoginRequiredMixin, ListView):
    model=Post
    template_name="Posteos/posteos_listar.html"

class PosteoDetalle(LoginRequiredMixin, DetailView):
    model=Post
    template_name="Posteos/posteos_detalle.html"

class PosteoCrear(LoginRequiredMixin, CreateView):
    model=Post
    success_url=reverse_lazy("posteos_listar")
    fields=["titulo","subtitulo","cuerpo","autor","imagen","fecha"]

class PosteoEdicion(LoginRequiredMixin, UpdateView):
    model=Post
    success_url=reverse_lazy("posteos_listar")
    fields=["titulo","subtitulo","cuerpo","autor","imagen","fecha"]

class PosteoEliminar(LoginRequiredMixin, DeleteView):
    model=Post
    success_url=reverse_lazy("posteos_listar")
    fields=["titulo","subtitulo","cuerpo","autor","imagen","fecha"]

#Profesores -------------------------------

class ProfesorList(LoginRequiredMixin, ListView):
    model=Profesor
    template_name="Posteos/profesor_listar.html"

class ProfesorDetalle(LoginRequiredMixin, DetailView):
    model=Profesor
    template_name="Posteos/profesor_detalle.html"

class ProfesorCrear(LoginRequiredMixin, CreateView):
    model=Profesor
    success_url=reverse_lazy("profesor_listar")
    fields=["nombre","apellido","email"]

class ProfesorEdicion(LoginRequiredMixin, UpdateView):
    model=Profesor
    success_url=reverse_lazy("profesor_listar")
    fields=["nombre","apellido","email"]

class ProfesorEliminar(LoginRequiredMixin, DeleteView):
    model=Profesor
    success_url=reverse_lazy("profesor_listar")
    fields=["nombre","apellido","email"]
