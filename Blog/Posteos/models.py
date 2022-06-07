from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
import datetime
from django.core.validators import MinValueValidator

class Post (models.Model): 
    titulo=models.CharField(max_length=300)
    subtitulo=models.CharField(max_length=300)
    cuerpo=RichTextField()
    autor=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to='media', null=True, default='', blank=True)
    #fecha=models.DateField(default=timezone.now)
    fecha=models.DateField(validators=[MinValueValidator(datetime.date.today)])
    
    def __str__(self):
        return f"Titulo: {self.titulo} -- Subtitulo: {self.subtitulo} -- Cuerpo: {self.cuerpo} --Autor: {self.autor} --Imagen: {self.imagen} --Fecha: {self.fecha}"

class Profesor (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} -- Apellido: {self.apellido} -- Email: {self.email}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatar', blank=True, null=True)
    def __str__(self):
        return f"User: {self.user} -- Avatar: {self.avatar}"

