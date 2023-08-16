from django.db import models


# Create your models here.

class Prensa(models.Model):


    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='prensa')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='Prensa'
        verbose_name_plural='Prensas'
        
    def __str__(self):
        return self.titulo
    
class imagePrensa(models.Model):
    imagen=models.ImageField(upload_to='galeria')

class imagePrensa(models.Model):
    prensa = models.ForeignKey(Prensa, on_delete=models.CASCADE)