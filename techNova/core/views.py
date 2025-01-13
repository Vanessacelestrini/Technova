from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required  # <-- Importação corrigida

# Lista de serviços
servicosLista = [
    {"nome": "Desenvolvimento Web", "descricao": "Criação de sites e apps", "preco": 2500.00},
    {"nome": "Consultoria", "descricao": "Análise de sistemas", "preco": 1800.00},
    {"nome": "Suporte Técnico", "descricao": "Suporte remoto e presencial", "preco": 500.00},
]

# Lista de cursos
cursosLista = [
    {"nome": "Python Básico", "descricao": "Introdução à programação com Python", "carga_horaria": 40, "preco": 800.00},
    {"nome": "Django Completo", "descricao": "Desenvolvimento web com Django", "carga_horaria": 60, "preco": 1200.00},
    {"nome": "Banco de Dados", "descricao": "Gestão de dados com SQL", "carga_horaria": 50, "preco": 1000.00},
]

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def cursos(request):
    return render(request, 'cursos.html', {'cursos': cursosLista})

def servicos(request):
    return render(request, 'servicos.html', {'servicos': servicosLista})

def produtos(request):
    produtos_lista = Produto.objects.all() 
    return render(request, 'produtos.html', {'produtos': produtos_lista})

def registrarUsuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            return render(request, 'registrar-usuario.html', {'form': form, 'error': 'Erro ao registrar, tente novamente.'})
    else:
        form = UserCreationForm()
    return render(request, 'registrar-usuario.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login-usuario.html', {'form': form})

@login_required
def servicos(request):
    return render(request, 'servicos.html', {'servicos': servicosLista})

@login_required
def cursos(request):
    return render(request, 'cursos.html', {'cursos': cursosLista})
