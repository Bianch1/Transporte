from django import forms
from .models import Pessoa

# class ChatForm(forms.ModelForm):
#     class Meta:
#         model = Chat
#         fields = ['pessoa', 'mensagem']
#         widgets = {
#             'pessoa': forms.Select(attrs={'style': 'width:100%; padding:8px;'}),
#             'mensagem': forms.Textarea(attrs={
#                 'rows':4,
#                 'placeholder':'Digite a mensagem/ocorrência...',
#                 'style':'width:100%; padding:8px;'
#             }),
#         }

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Nome da pessoa...','style':'width:100%; padding:8px;'}),
        }
