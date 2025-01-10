from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Registrar novo usuário
def registrarUsuario(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            return render(request, 'registrar-usuario.html', {'erro': 'As senhas não coincidem.'})

        # Verificar se o nome de usuário já existe
        if get_user_model().objects.filter(username=nome_usuario).exists():
            return render(request, 'registrar-usuario.html', {'erro': 'Este nome de usuário já está em uso.'})

        # Verificar se o e-mail já está em uso
        if get_user_model().objects.filter(email=email).exists():
            return render(request, 'registrar-usuario.html', {'erro': 'Este e-mail já está em uso.'})

        # Criar o usuário
        user = get_user_model().objects.create_user(username=nome_usuario, email=email, password=senha)
        return redirect('login')  # Redireciona para a página de login após o registro

    return render(request, 'registrar-usuario.html')

def home(request):
    return render(request, 'home.html')

def login_usuario(request):
    return render(request, 'login.html')

def custom_logout(request):
    return render(request, 'deslogar-usuario.html')

def listar_produtos(request):
    return render(request, 'listar-produtos.html')

def cadastrar_produto(request):
    return render(request, 'cadastrar-produto.html')