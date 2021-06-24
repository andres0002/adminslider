from django.db import models

# Create your models here.

class Slider(models.Model):
    '''Esta clase se encarga de definir los actributos de la tabla Categoria de la base de datos ryvatec.'''
    slug = models.CharField(max_length=30)
    image = models.ImageField(upload_to='sliders', blank=False, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__
        return self.slug

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"