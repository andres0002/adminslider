from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render, redirect
from apps.base.models import Slider
from apps.user.forms import SliderForm

# Create your views here.

class Home(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar la plantilla de inicio o landing page.'''
    template_name = 'home/home.html'

    def get_queryset(self):
        return Slider.objects.all()

    def get_context_data(self, **kwargs):
        context =  {}
        context['sliders'] = self.get_queryset()
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

class ListSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar una lista de todos los sliders registrados en el sistema.'''
    template_name = 'list_slider.html'

    def get_queryset(self):
        return Slider.objects.all()

    def get_context_data(self, **kwargs):
        context =  {}
        context['sliders'] = self.get_queryset()
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

class AddSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga  de adicionar los sliders.'''
    template_name = 'add_slider.html'
    form_class = SliderForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El slider se adicionó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El slider no se pudo adicionar')
        return redirect('admin_slider:list_sliders')

class VisualizeSlider(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de visualizar el slider.
    '''
    template_name = 'visualize_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        slider = Slider.objects.get(id=id)
        form = self.form_class(instance=slider)
        return render(request, self.template_name, {'form': form})

class UpdateSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de modificar el slider.'''
    template_name = 'update_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        slider = Slider.objects.get(id=id)
        form = self.form_class(instance=slider)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        slider = Slider.objects.get(id=id)
        form = self.form_class(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El slider se modificó correctamente')
        else:
            messages.add_message(request, messages.ERROR, 'El slider no se pudo modificar')
        return redirect('admin_slider:list_sliders')

class DeleteSlider(LoginRequiredMixin, View):
    '''Esta clase se encarga de borrar el slider.'''
    template_name = 'delete_slider.html'
    form_class = SliderForm

    def get(self, request, id):
        slider = Slider.objects.get(id=id)
        form = self.form_class(instance=slider)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        slider = Slider.objects.get(id=id)
        slider.delete()
        messages.add_message(request, messages.INFO, "El slider se borró correctamente")
        return redirect('admin_slider:list_sliders')