from django import forms
from apps.user.models import User

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = (
            "name",
            "last_name",
            "usuid",
            "rol"
        )
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'usuid': 'Username',
            'rol': 'Tipo de usuario'
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(UserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})