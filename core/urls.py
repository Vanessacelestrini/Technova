from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar-usuario/', views.registrarUsuario, name='registrar-usuario'),
    path('logout/', views.custom_logout, name='deslogar-usuario'),
    path('login/', views.login_usuario, name='login'), 
    path('produtos/', views.listar_produtos, name='listar-produtos'),  
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar-produto'),  
]

