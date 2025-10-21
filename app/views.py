from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
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
    







# # Alterações feias para criar o chat
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required, user_passes_test

# def staff_required(user):
#     return user.is_active and user.is_staff

# @login_required
# @user_passes_test(staff_required)
# def chat(request):
#     """
#     Página única: lista de chats + formulário para adicionar Chat + formulário para adicionar Pessoa.
#     Acesso restrito a staff (admin).
#     """
#     chats = Chat.objects.select_related('pessoa').all()
#     pessoas = Pessoa.objects.all().order_by('nome')

#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')
#         if form_type == 'chat':
#             chat_form = ChatForm(request.POST)
#             pessoa_form = PessoaForm()
#             if chat_form.is_valid():
#                 chat_form.save()
#                 return redirect('chat:pagina')
#         elif form_type == 'pessoa':
#             pessoa_form = PessoaForm(request.POST)
#             chat_form = ChatForm()
#             if pessoa_form.is_valid():
#                 pessoa_form.save()
#                 return redirect('chat:pagina')
#         else:
#             chat_form = ChatForm()
#             pessoa_form = PessoaForm()
#     else:
#         chat_form = ChatForm()
#         pessoa_form = PessoaForm()

#     return render(request, 'chat/chat.html', {
#         'chats': chats,
#         'pessoas': pessoas,
#         'chat_form': chat_form,
#         'pessoa_form': pessoa_form,
#     })
