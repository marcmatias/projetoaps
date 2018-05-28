from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *




class IndexListView(generic.TemplateView):
	template_name = 'sistema/index.html'

# CRUD Estabelecimento

class EstabelecimentoListView(generic.ListView):
    model = Estabelecimento
    template_name = 'gerenciamento/estabelecimento_listar.html'

class EstabelecimentoCreateView(generic.CreateView):
	model = Estabelecimento
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['nome']
	success_url = reverse_lazy('sistema:estabelecimento_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar Estabelecimento"
		return super().get_context_data(**context)

class EstabelecimentoUpdateView(generic.UpdateView):
	model = Estabelecimento
	template_name = 'gerenciamento/editar.html'
	fields = ['nome']
	success_url = reverse_lazy('sistema:estabelecimento_listar')

	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar Estabelecimento"
		return super().get_context_data(**context)

class EstabelecimentoDeleteView(generic.DeleteView):
	model = Estabelecimento
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:estabelecimento_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Estabelecimento"
		return super().get_context_data(**context)


# Fim do CRUD Estabelecimento

# CRUD PRÉDIOS

class PredioListView(generic.ListView):
    model = Predio
    template_name = 'gerenciamento/predio_listar.html'

class PredioCreateView(generic.CreateView):
	model = Predio
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['estabelecimento', 'nome']
	success_url = reverse_lazy('sistema:predio_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar Prédio"
		return super().get_context_data(**context)

class PredioUpdateView(generic.UpdateView):
	model = Predio
	template_name_suffix = '_editar_form'
	template_name = 'gerenciamento/editar.html'
	fields = ['estabelecimento', 'nome']
	success_url = reverse_lazy('sistema:predio_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar Prédio"
		return super().get_context_data(**context)

class PredioDeleteView(generic.DeleteView):
	model = Predio
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:predio_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Prédio"
		return super().get_context_data(**context)

# Fim do CRUD PRÉDIOS
