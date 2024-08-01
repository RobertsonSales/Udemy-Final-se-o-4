from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem - Até 300 caracteres, incluindo espaços', widget=forms.Textarea(), max_length=300)

    def send_mail(self):
        nome=self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}'
        mail = EmailMessage(
            subject='E-mail enviado pelo distema Django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()
class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome','preco','estoque', 'imagem']
