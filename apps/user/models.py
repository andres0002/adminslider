from django.contrib.auth.models import User
from django.db import models

# Create your models here.

ROL_CHOICES = (
    ('AMD', u'Administrador'),
)

class User(models.Model):
    '''
    Esta clase se encarga de definir los actributos de la tabla Usuario de la base de datos ryvatec.
    '''
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
