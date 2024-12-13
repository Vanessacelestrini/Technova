from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('cursos', views.cursos, name='cursos'),
    path('servicos', views.servicos, name='servicos')
]
