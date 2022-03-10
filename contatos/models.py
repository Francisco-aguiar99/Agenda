from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
"""
CONTATOS
Nome: STR * (obrigatorio)
sobrenome: STR (opcional)
telefone: STR * (obrigatorio)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria:  CATEGORIA (outra model)

CATEGOTIA
ID: INT
NOME: STR * (OBRIGATORIO)

"""


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d')

    """
    Qundo adicionar qualquer coisa no models
     tem que fazer a python manage.py makemigrations
     e quando for add field 
     python manage.py migrate
    """

    def __str__(self):
        return self.\
            nome









