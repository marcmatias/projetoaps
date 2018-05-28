from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django import forms


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
		context['breadcrumb_title'] = "Estabelecimento"
		context['breadcrumb_link'] = "estabelecimento_listar"
		return super().get_context_data(**context)

class EstabelecimentoUpdateView(generic.UpdateView):
	model = Estabelecimento
	template_name = 'gerenciamento/editar.html'
	fields = ['nome']
	success_url = reverse_lazy('sistema:estabelecimento_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar Estabelecimento"
		context['breadcrumb_title'] = "Estabelecimento"
		context['breadcrumb_link'] = "estabelecimento_listar"
		return super().get_context_data(**context)

class EstabelecimentoDeleteView(generic.DeleteView):
	model = Estabelecimento
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:estabelecimento_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Estabelecimento"
		context['breadcrumb_title'] = "Estabelecimento"
		context['breadcrumb_link'] = "estabelecimento_listar"
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
		context['breadcrumb_title'] = "Prédio"
		context['breadcrumb_link'] = "predio_listar"
		return super().get_context_data(**context)

class PredioUpdateView(generic.UpdateView):
	model = Predio
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

# CRUD SALAS

class SalaListView(generic.ListView):
    model = Sala
    template_name = 'gerenciamento/sala_listar.html'

class SalaCreateView(generic.CreateView):
	model = Sala
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['predio', 'nome']
	success_url = reverse_lazy('sistema:sala_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar Sala"
		context['breadcrumb_title'] = "Sala"
		context['breadcrumb_link'] = "sala_listar"
		return super().get_context_data(**context)

class SalaUpdateView(generic.UpdateView):
	model = Sala
	template_name = 'gerenciamento/editar.html'
	fields = ['predio', 'nome']
	success_url = reverse_lazy('sistema:sala_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar Sala"
		return super().get_context_data(**context)

class SalaDeleteView(generic.DeleteView):
	model = Sala
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:sala_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Sala"
		return super().get_context_data(**context)

# Fim do CRUD SALAS

# CRUD consumo

class ConsumoListView(generic.ListView):
    model = Consumo
    template_name = 'gerenciamento/consumo_listar.html'

class ConsumoCreateView(generic.CreateView):
	model = Consumo
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['sala', 'kwh', 'data']
	success_url = reverse_lazy('sistema:consumo_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar consumo"
		context['breadcrumb_title'] = "Consumo"
		context['breadcrumb_link'] = "consumo_listar"
		return super().get_context_data(**context)
	# def get_form(self, form_class=None):
	# 	form = super(ConsumoCreateView, self).get_form(form_class)
	# 	form.fields['data'].widget.attrs.update({'class': 'datepicker'})
	# 	return form

class ConsumoUpdateView(generic.UpdateView):
	model = Consumo
	template_name = 'gerenciamento/editar.html'
	fields = ['sala', 'kwh', 'data']
	success_url = reverse_lazy('sistema:consumo_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar Consumo"
		return super().get_context_data(**context)


class ConsumoDeleteView(generic.DeleteView):
	model = Consumo
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:consumo_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Consumo"
		return super().get_context_data(**context)

# Fim do CRUD consumo
