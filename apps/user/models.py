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
    email = models.EmailField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='user', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):  # __unicode__
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
