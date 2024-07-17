from django.shortcuts import render
from .forms import Cliente
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'pages/paginas/home.html')

def menu(request):
    return render(request, 'pages/paginas/menu.html')

def cardapio(request):
    return render(request, 'pages/paginas/cardapio.html')

def indexcadastrado(request):

    return render(request, 'pages/paginas/indexcadastrado.html')

@login_required(login_url='auth/login')
def Cliente(request):
    form = Cliente(request.POST)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        idade = form.cleaned_data['idade']
    else:
        form = Cliente()

    return render(request, 'pages/paginas/cadastro.html',{'form': form})

def pagamento(request):
    return render(request, 'pages/paginas/pagamento.html',)

def contato(request):
    return render(request, 'pages/paginas/contato.html')

def compra(request):
    return render(request, 'pages/paginas/compra.html')

def cadastro(request):
     return render(request, 'pages/paginas/cadastro.html')

def login(request):
     return render(request, 'pages/paginas/login.html')

