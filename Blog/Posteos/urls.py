from django.urls import path
from Posteos import views
from .views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.AcercaDeMi, name='about'),
    path('comodin', views.comodin, name='comodin'),
   
    path('login',views.req_login, name='login'),
    path('register',views.register, name='register'),
    path('logout', LogoutView.as_view(template_name="Posteos/logout.html"), name='logout'),

    path('editarperfil', editarPerfil, name='editarperfil'),
    path('agregarElAvatar', agregarAvatar, name='agregarElAvatar'),

    path('list/', ProfesorList.as_view(), name='profesor_listar'),
    path('Profesores/<pk>', ProfesorDetalle.as_view(), name='profesor_detalle'),
    path('Profesores/nuevo/', ProfesorCrear.as_view(), name='profesor_crear'),
    path('Profesores/editar/<pk>', ProfesorEdicion.as_view(), name='profesor_editar'),
    path('Profesores/borrar/<pk>', ProfesorEliminar.as_view(), name='profesor_borrar'),

    path('Posteo/list/', PosteoList.as_view(), name='posteos_listar'),
    path('Posteo/<pk>', PosteoDetalle.as_view(), name='posteos_detalle'),
    path('Posteo/nuevo/', PosteoCrear.as_view(), name='posteos_crear'),
    path('Posteo/editar/<pk>', PosteoEdicion.as_view(), name='posteos_editar'),
    path('Posteo/borrar/<pk>', PosteoEliminar.as_view(), name='posteos_borrar'),
]


   
