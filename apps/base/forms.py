from django import forms
from apps.base.models import Slider
from apps.user.models import ROL_CHOICES

class SliderForm(forms.Form):
    class Meta:
        model = Slider
        fields = (
            "slug",
            "image"
        )
        labels = {
            'slug': 'Slug de la imagen',
            'image': 'Imagen del slider'
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(SliderForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AddUserForm(forms.Form):
    '''Esta clase se encarga de definir la estructura del formulario de datos del usuario.'''
    username = forms.CharField(max_length=150, label='Username')
    email = forms.EmailField(max_length=150, label='Email')
    password = forms.CharField(max_length=128, label='Contraseña', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, label='Confirmar Contraseña', widget=forms.PasswordInput())
    name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')
    rol = forms.ChoiceField(choices=ROL_CHOICES, label='Tipo de Ususario', widget=forms.Select())

    def __init__(self, *args, **kwargs):
        '''
        Esta funcion se encarga de darle el diseño al formulario.
        :param args: La cantidad de argumentos que recibe.
        :param kwargs: Se encarga de tomar los parametros de la url.
        '''
        super(AddUserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})