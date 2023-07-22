from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    parrafo = models.TextField()
    fecha_posteada = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        ordering = ["-titulo"]

    def __str__(self):
        return f'\n Titulo: {self.titulo} \n parrafo: {self.parrafo} \n autor: {self.autor} \n fecha posteada: {self.fecha_posteada}'

    def get_absolute_url(self):
        return reverse('Post-Detalle', kwargs={'pk': self.pk})
