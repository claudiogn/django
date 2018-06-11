from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil, Convite
# from bitcoins.models import perfil

# Create your views here.
def index(request):
	perfis=Perfil.objects.all()
	return render(request, 'index.html', {"perfis": perfis, "perfil_logado": get_perfil_logado(request)})


def exibir(request, perfil_id):
	perfil=Perfil.objects.get(id=perfil_id)
	perfil_logado=get_perfil_logado(request)
	ja_e_contato= perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html', {"perfil": perfil, "ja_e_contato": ja_e_contato})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado=	get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

def termos_e_condicoes(request):
	return render(request, 'termos_e_condicoes.html')

def politica_de_privacidade(request):
	return render(request, 'politica_de_privacidade.html')


def politica_de_reembolso(request):
	return render(request, 'politica_de_reembolso.html')

def contato(request):
	return render(request, 'contato.html')

def aceitar(request, convite_id):
	convite=Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')


def get_perfil_logado(request):
	return Perfil.objects.get(id=1)