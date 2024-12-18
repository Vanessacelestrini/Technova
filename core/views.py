from django.shortcuts import render
from .models import Servico, Curso
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def cursos(request): 
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def servicos(request):
    servicos = Servico.objects.all()  # Busca todos os registros da tabela Servico
    return render(request, 'servicos.html', {'servicos': servicos})

def registrarUsuario(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render('registrar-usuario.html')
    else:
        form = UserCreationForm()
    return render(request, 'registrar-usuario.html', {'form': form})

    
            