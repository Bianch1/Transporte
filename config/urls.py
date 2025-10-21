"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # Demais Urls
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('veiculos/', VeiculosView.as_view(), name='veiculos'),
    path('tipo/',TiposTransporteView.as_view(), name='Tipos de Transporte'),
    path('rotas/', RotasView.as_view(), name='rotas'),
    path('instituicoes/',InstituicoesView.as_view(), name='instituicoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('horarios/', HorariosView.as_view(), name='horarios'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('gastos/',GastosView.as_view(), name='gastos'),

    # path('chat/', chat, name='chat'),   # /chat/
]