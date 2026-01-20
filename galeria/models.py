from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#login teste - 123
# Create your models here.
class Fotografia(models.Model):

    opcoes_categoria = [
        ('NEBULOSA','Nebulosa'),
        ('ESTRELA','Estrela'),
        ('GALAXIA','Galaxia'),
        ('PLANETA','Planeta'),
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    categoria = models.CharField(max_length=50, choices=opcoes_categoria, default='')
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return self.nome
