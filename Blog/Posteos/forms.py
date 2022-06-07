
from unittest.util import _MAX_LENGTH
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Crear_Posteos(forms.Form):
  titulo=forms.CharField(max_length=50)
  subtitulo=forms.CharField(max_length=50)
  cuerpo=forms.CharField(max_length=500)
  autor=forms.CharField(max_length=50)
  imagen= forms.ImageField()
  fecha=forms.DateField()

class formulario_Profesor(forms.Form):
  nombre=forms.CharField(max_length=50)
  apellido=forms.CharField(max_length=50)
  email=forms.EmailField()

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar la contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
        help_texts={ayuda:"" for ayuda in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Modificar la contraseña.",widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar la contraseña.",widget=forms.PasswordInput)
    last_name= forms.CharField(label="Modificar el apellido.")
    first_name= forms.CharField(label="Modificar el nombre.")
    class Meta:
        model=User
        fields=('email', 'password1', 'password2', 'last_name', 'first_name')
        help_texts={h:"" for h in fields}

class AvatarForm(forms.Form):
  avatar= forms.ImageField(label="Avatar")

