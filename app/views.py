from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})


class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})


class TiposTransporteView(View):
    def get(self, request, *args, **kwargs):
        tipos = Tipo.objects.all()
        return render(request, 'tipo.html', {'tipos': tipos})


class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})


class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})


class VeiculosView(View):
    def get(self, request, *args, **kwargs):
        veiculos = Veiculo.objects.all()
        return render(request, 'veiculos.html', {'veiculos': veiculos})


class RotasView(View):
    def get(self, request, *args, **kwargs):
        rotas = Rota.objects.all()
        return render(request, 'rotas.html', {'rotas': rotas})


class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})


class HorariosView(View):
    def get(self, request, *args, **kwargs):
        horarios = Horario.objects.all()
        return render(request, 'horarios.html', {'horarios': horarios})


class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})


class GastosView(View):
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all()
        return render(request, 'gastos.html', {'gastos': gastos})
