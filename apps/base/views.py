# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import auth
from django.contrib import messages
from apps.user.models import User
from apps.base.models import Slider
from apps.base.forms import AddUserForm

# Create your views here.

class Login(View):
    template_name = 'login.html'
    '''Esta clase se encarga del logeo del usuario, de verificar que el usuario y la contraseña sean correctas.'''
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla del login.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla login.
        '''
        return render(request, self.template_name)

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el usuario y la contraseña sean correctas.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla correspondiente al usuario y si se presenta un error
        o inconveniente nos retorna la plantilla login.
        '''
        username = request.POST.get("signin_username")
        password = request.POST.get("signin_password")
        usuario = auth.authenticate(username=username, password=password)

        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            cliente = User.objects.filter(usuid=usuario.pk)

            if cliente[0].rol == "AMD":
                return redirect('admin_slider:home')

            else:
                messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no se encuentra registrado")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, self.template_name)


class Logout(View):
    '''Esta clase se encarga de mostrar el login.'''
    def get(self, request):
        '''
        Esta clase se encarga de mostrar la plantilla login.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla login.
        '''
        auth.logout(request)
        return redirect('login')

class Home(View):
    '''Esta clase se encarga de mostrar la plantilla de inicio o landing page sin logeo.'''
    template_name = 'home.html'

    def get(self, request):
        '''
                    Esta funcion se encarga de mostrar todos los sliders.
                    :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                    :return: Nos retorna la plantilla de inicio y todos los sliders registrados en el sistema.
                    '''
        sliders = Slider.objects.all()
        return render(request, self.template_name, {'sliders': sliders})

class AddUser(View):
    '''Esta clase se encarga de agregar los usuarios.'''
    template_name = 'add_user.html'
    form_class = AddUserForm

    def get(self, request):
        '''
        Esta funcion se encarga de mostrarnos la plantilla de adicionar usuario y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla adicionar usuario y su respectivo formulario.
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el usuario se agrego correctamente o de lo contrario si se precento
        algun inconveniente o error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna a la plantilla adicionar usuario.
        '''
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            confirm_password = request.POST.get('confirm_password', None)
            name = request.POST.get('name', None)
            last_name = request.POST.get('last_name', None)
            rol = request.POST.get('rol', None)

            if password == confirm_password:
                if username and email and password and confirm_password:
                    user, created = User.objects.get_or_create(username=username,
                                                                email=email,
                                                                first_name=name,
                                                                last_name=last_name)

                    if created:
                        user.set_password(password)
                        user.save()
                        cliente = User(
                                        name=name,
                                        last_name=last_name,
                                        rol=rol,
                                        usuid=user)
                        cliente.save()
                        messages.add_message(request, messages.INFO, "El usuario se agrego satisfactoriamente")
                        return redirect('login')

                    else:
                        messages.add_message(request, messages.ERROR, "El usuario ya existe en el sistema")

                else:
                    messages.add_message(request, messages.ERROR, "Faltan campos por llenar en el formulario")

            else:
                messages.add_message(request, messages.ERROR, "Verifique las contraseña")
        return render(request, self.template_name, {'form': form})