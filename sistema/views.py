from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django import forms
import datetime
from datetime import date, datetime, timedelta



# Fim de alterar usuário

class IndexListView(generic.TemplateView):
	template_name = 'sistema/index.html'


class ChartListView(generic.TemplateView):
	template_name = 'sistema/chart.html'
	def get_context_data(self, **kwargs):
		context = {}
		context['salas'] = Sala.objects.all()
		return super().get_context_data(**context)
	def post(self, request):
		context = {}
		context['salas'] = Sala.objects.all()
		context['select_sala'] = request.POST['select_sala']
		context['sala'] = Sala.objects.get(slug=context['select_sala'])
		# Gráfico de Consumo diário
		context['consumo'] = Consumo.objects.filter(sala=context['sala']).order_by('data')
		# Gráfico de histórico de consumo mensal
		one_month_before = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1)
		two_month_before = (one_month_before - timedelta(days=1)).replace(day=1)
		three_month_before = (two_month_before - timedelta(days=1)).replace(day=1)
		four_month_before = (three_month_before - timedelta(days=1)).replace(day=1)
		five_month_before = (four_month_before - timedelta(days=1)).replace(day=1)
		six_month_before = (five_month_before - timedelta(days=1)).replace(day=1)
		context['consumo_one_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=one_month_before.strftime("%m"))
		context['consumo_two_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=two_month_before.strftime("%m"))
		context['consumo_three_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=three_month_before.strftime("%m"))
		context['consumo_four_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=four_month_before.strftime("%m"))
		context['consumo_five_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=five_month_before.strftime("%m"))
		context['consumo_six_month_before'] = Consumo.objects.filter(sala=context['sala'], data__month=six_month_before.strftime("%m"))
		consumo_month = 0
		for consumo in context['consumo_one_month_before']:
			consumo_month += consumo.kwh 
		# print(context['consumo_one_month_before'])
		return render(request, self.template_name, context)

# CRUD Estabelecimento

# class EstabelecimentoListView(generic.ListView):
#     model = Estabelecimento
#     template_name = 'gerenciamento/listar/estabelecimento_listar.html'
#
# class EstabelecimentoCreateView(generic.CreateView):
# 	model = Estabelecimento
# 	template_name = 'gerenciamento/cadastrar.html'
# 	fields = ['nome']
# 	success_url = reverse_lazy('sistema:estabelecimento_listar')
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Cadastrar Estabelecimento"
# 		context['breadcrumb_title'] = "Estabelecimento"
# 		context['breadcrumb_link'] = "estabelecimento_listar"
# 		return super().get_context_data(**context)
#
# class EstabelecimentoUpdateView(generic.UpdateView):
# 	model = Estabelecimento
# 	template_name = 'gerenciamento/editar.html'
# 	fields = ['nome']
# 	success_url = reverse_lazy('sistema:estabelecimento_listar')
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Editar Estabelecimento"
# 		context['breadcrumb_title'] = "Estabelecimento"
# 		context['breadcrumb_link'] = "estabelecimento_listar"
# 		return super().get_context_data(**context)
#
# class EstabelecimentoDeleteView(generic.DeleteView):
# 	model = Estabelecimento
# 	template_name = 'gerenciamento/deletar.html'
# 	success_url = reverse_lazy('sistema:estabelecimento_listar')
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Deletar Estabelecimento"
# 		context['breadcrumb_title'] = "Estabelecimento"
# 		context['breadcrumb_link'] = "estabelecimento_listar"
# 		return super().get_context_data(**context)


# Fim do CRUD Estabelecimento

# CRUD PRÉDIOS

class PredioListView(generic.ListView):
    model = Predio
    template_name = 'gerenciamento/listar/predio_listar.html'

class PredioCreateView(generic.CreateView):
	model = Predio
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['nome']
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
	fields = ['nome']
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
    template_name = 'gerenciamento/listar/sala_listar.html'

class SalaCreateView(generic.CreateView):
	model = Sala
	template_name = 'gerenciamento/cadastrar.html'
	# fields = ['predio', 'nome']
	form_class = SalaForm
	success_url = reverse_lazy('sistema:sala_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['predios'] = Predio.objects.all()
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
		context['predios'] = Predio.objects.all()
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
    template_name = 'gerenciamento/listar/consumo_listar.html'

class ConsumoCreateView(generic.CreateView):
	model = Consumo
	template_name = 'gerenciamento/cadastrar.html'
	form_class = ConsumoForm
	success_url = reverse_lazy('sistema:consumo_listar')
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar consumo"
		context['breadcrumb_title'] = "Consumo"
		context['breadcrumb_link'] = "consumo_listar"
		return super().get_context_data(**context)
	# Modificar field do formulário
	# def get_form(self, form_class=None):
	# 	form = super(ConsumoCreateView, self).get_form(form_class)
	# 	form.fields['data'].widget.attrs.update({'class': 'datepicker'})
	# 	return form

class ConsumoUpdateView(generic.UpdateView):
	model = Consumo
	template_name = 'gerenciamento/editar.html'
	form_class = ConsumoForm
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

# Popular select sala
def load_salas(request):
    predio_id = request.GET.get('predio')
    salas = Sala.objects.filter(predio__pk=predio_id)
    return render(request, 'hr/salas_dropdown_list_options.html', {'salas': salas})
