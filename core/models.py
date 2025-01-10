<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  
        blank=True
    )

    def __str__(self):
        return self.username

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()  # Exemplo de atributo de carga horária
    preco = models.DecimalField(max_digits=10, decimal_places=2)
=======
# core/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.CharField(max_length=255, null=True, blank=True)  # Pode ser ForeignKey, dependendo do caso
>>>>>>> 08d80c2 (atualizado)

    def __str__(self):
        return self.nome
