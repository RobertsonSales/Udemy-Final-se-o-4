from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto
from django.shortcuts import redirect

#Importa os dois form-models

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)
def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.success(request, 'E-mail não enviado! Preencha os campos adequadamente.')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                prod = form.save(commit=False)
                form.save() #Salva os registros no banco de dados
                messages.success(request, 'Produto salvo com sucesso: '+str({prod.nome})+'!')
                form = ProdutoModelForm()  #Limpa o formulário
            else:
                messages.success(request, 'Erro ao salvar o produto! Tente novamente.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
       return redirect('index')