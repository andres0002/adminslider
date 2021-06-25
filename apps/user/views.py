from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render, redirect
from apps.user.models import User
from apps.base.models import Slider
from apps.user.forms import UserForm
from apps.base.forms import SliderForm

# Create your views here.

class ListSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar una lista de todos los sliders registrados en el sistema.'''
    template_name = 'list_slider.html'
    form_class = SliderForm

    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla de listar Sliders.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de listar Sliders y la respectiva lista de las Sliders.
        '''
        sliders = Slider.objects.all()
        return render(request, self.template_name, {'sliders': sliders})

class AddSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga  de adicionar los sliders.'''
    template_name = 'add_slider.html'
    form_class = SliderForm

    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla de adicionar slider y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de adicionar slider y  su respectivo formulario.
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar si el slider se adiciono correctamente o de lo contrario si se precento algun inconveniente o error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la lista de todos los sliders registrados en el sistema.
        '''
        try:
            form = self.form_class(request.POST)

            if form.is_valid:
                form.save()
                messages.add_message(request, messages.INFO, 'El Slider se adicionó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Slider no se pudo adicionar')

        except Slider.DoesNotExist:
            return render(request, "pages-404.html")

        return redirect("admin_slider:list_sliders")

class VisualizeSlider(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de visualizar el slider.
    '''
    template_name = 'visualize_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        '''
        Esta funcion se encarga de visualizar el slider selecionada.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id: Este actributo sirve para identificar el slider que deseamos visualizar.
        :return: Nos retorna la plantilla visualizar slider y  su respectivo formulario.
        '''
        slider = Slider.objects.get(id=id)
        form = self.form_class(instance=slider)
        return render(request, self.template_name, {'form': form})

class UpdateSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de modificar el slider.'''
    template_name = 'update_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        '''
        Esta funcion se encarga de mostrar la plantilla modificar slider y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id: Este actributo sirve para identificar el slider que deseamos modificar.
        :return: Nos retorna la plantilla modificar slider y su respectivo formulario.
        '''
        slider = Slider.objects.get(id=id)
        form = self.form_class(instance=slider)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        '''
        Esta funcion se encarga de verificar que el slider se alla modificado correctamente o  de lo contrario si se precento un error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id: Este actributo sirve para identificar el slider que se desea modificar.
        :return: Nos retorna la lista de todas los slider registrados en el sistema.
        '''
        slider = Slider.objects.get(id=id)
        form = self.form_class(data=request.POST, instance=slider)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El slider se modificó correctamente')
            return redirect("admin_slider:list_sliders")

        else:
            messages.add_message(request, messages.ERROR, 'El slider no se pudo modificar')

        return redirect("admin_slider:list_sliders")

class DeleteSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de borrar el slider.'''
    template_name = 'delete_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        '''
        Esta funcion nos muestra la plantilla borrar slider y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id: Este actributo sirve para identificar el slider que desea eliminar.
        :return: Nos retorna la plantilla borrar slider y su respectivo formulario.
        '''
        try:
            slider = Slider.objects.get(id=id)
            form = self.form_class(instance=slider)
            return render(request, self.template_name, {'form': form})

        except Slider.DoesNotExist:
            return redirect("admin_slider:list_sliders")

    def post(self, request, id):
        '''
        Esta funcionse encarga de verificar que el slider se alla borrado correctamente o de lo contrario si se precento algun inconveniente.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id: Este actributo sirve para identificar el slider que se desea eliminar.
        :return: Nos retorna la lista de todas las categorias registradas en el sistema.
        '''
        slider = Slider.objects.get(id=id)
        slider.delete()
        messages.add_message(request, messages.INFO, "El slider se borró correctamente")

        return redirect("admin_slider:list_sliders")

class Home(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar la plantilla de inicio o landing page.'''
    template_name = 'home/home.html'
    def get(self, request):
        '''
                    Esta funcion se encarga de mostrar la plantilla de inicio o landing page.
                    :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                    :return: Nos retorna la plantilla de inicio o landing page.
                    '''
        sliders = Slider.objects.all()
        return render(request, self.template_name, {'sliders': sliders})
