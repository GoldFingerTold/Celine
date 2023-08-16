from django.db import models

# Create your models here.

class News(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='news')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='News'
        verbose_name_plural='Newss'
        
    def __str__(self):
        return self.titulo

