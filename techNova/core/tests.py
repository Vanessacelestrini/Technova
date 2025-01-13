from django.test import TestCase
from .models import Servico, Curso

class ServicoModelTest(TestCase):
    def setUp(self):
        Servico.objects.create(nome="Teste", descricao="Descrição de teste", preco=100.00)

    def test_servico_nome(self):
        servico = Servico.objects.get(nome="Teste")
        self.assertEqual(servico.nome, "Teste")

class CursoModelTest(TestCase):
    def setUp(self):
        Curso.objects.create(nome="Curso Teste", descricao="Descrição do curso teste", carga_horaria=10, preco=200.00)

    def test_curso_nome(self):
        curso = Curso.objects.get(nome="Curso Teste")
        self.assertEqual(curso.nome, "Curso Teste")
