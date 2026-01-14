from django.db import models
from datetime import datetime
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
    foto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=opcoes_categoria, default='')
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
