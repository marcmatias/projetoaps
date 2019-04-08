from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django import forms
from .models import *
from .forms import *
from datetime import datetime, timedelta
import calendar
import arrow
import collections
# Rest and Serializers
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# User Create 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from calendar import month_name, different_locale

import json

class IndexListView(generic.TemplateView):
	template_name = 'sistema/index.html'

class ChartListView(generic.TemplateView):
	template_name = 'sistema/chart.html'
	
	def authenticated(self, user):
		return self.filter(user=user)
	
	def get_context_data(self):
		context = {}
		# Poulando select de acordo com usuário logado
		if self.request.user.username == "admin": context['salas'] = Sala.objects.all()
		else: context['salas'] = Sala.objects.filter(estabelecimento__user__username=self.request.user)
		return context
	
	def post(self, request):
		context = {}

		for s in self.get_context_data().values(): salasSelect = s

		context['salas'] = salasSelect

		context['select_sala'] = request.POST['select_sala']
		context['sala'] = Sala.objects.get(slug=context['select_sala'])

		# # Gráfico de histórico de consumo mensal
		date = arrow.now()
		# Mês atual usado como referencia para obter meses anteriores
		month_conunting = date.replace(day=1)

		# Listando ultimos meses en relação ao atual
		months_list_name = []
		months_list_number = []
		month_dict = {get_month_name(int(month_conunting.strftime("%m"))) : month_conunting}
		months_list_name.insert(0, get_month_name(int(month_conunting.strftime("%m"))) + "/" + month_conunting.strftime("%y"))
		months_list_number.insert(0, int(month_conunting.strftime("%m")))
		for x in range(5):
			month = (month_conunting - timedelta(days=1)).replace(day=1)
			month_name = get_month_name(int(month.strftime("%m"))) + "/" + month.strftime("%y")
			months_list_name.insert(0, month_name)
			months_list_number.insert(0, int(month.strftime("%m")))
			month_dict[month_name] = month
			month_conunting = month
		context['meses'] = months_list_name
		
		# Listando consumo de salas ao longo dos meses
		sala_consumo = []
		for m in months_list_number:
			consumo_mes_anterior = sum(Consumo.kwh for Consumo in (Consumo.objects.filter(sala=context['sala'],
			 	data__month=m)))
			sala_consumo.insert(0, consumo_mes_anterior)

		context['sala_consumo'] = sala_consumo[::-1]
		it = iter(sala_consumo)
		context['preco_last_month'] = (next(it) / 100) * 2
		context['preco_2last_month'] = (next(it) / 100) * 2
		context['preco_3last_month'] = (next(it) / 100) * 2
		context['30_days'] = thirty_day(context['sala'])
		return render(request, self.template_name, context)

# CRUD Estabelecimento

class EstabelecimentoListView(generic.ListView):
    model = Estabelecimento
    template_name = 'gerenciamento/listar/estabelecimento_listar.html'

class EstabelecimentoCreateView(generic.CreateView):
	model = Estabelecimento
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['nome', 'user']
	success_url = reverse_lazy('sistema:estabelecimento_listar')
	def get_context_data(self):
		context = {}
		context['title'] = "Cadastrar Estabelecimento"
		context['breadcrumb_title'] = "Estabelecimento"
		context['breadcrumb_link'] = "estabelecimento_listar"
		return super().get_context_data(**context)

class EstabelecimentoUpdateView(generic.UpdateView):
	model = Estabelecimento
	template_name = 'gerenciamento/editar.html'
	fields = ['nome', 'user']
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
    template_name = 'gerenciamento/listar/predio_listar.html'

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
		context['breadcrumb_link'] = "predio_listar"
		return super().get_context_data(**context)

class PredioDeleteView(generic.DeleteView):
	model = Predio
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:predio_listar')
	
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Prédio"
		context['breadcrumb_link'] = "predio_listar"
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
	fields = ['estabelecimento', 'predio', 'nome']
	success_url = reverse_lazy('sistema:sala_listar')
	
	def get_context_data(self, **kwargs):
		context = {}
		context['predios'] = Predio.objects.all()
		context['title'] = "Editar Sala"
		context['breadcrumb_link'] = "sala_listar"
		return super().get_context_data(**context)

class SalaDeleteView(generic.DeleteView):
	model = Sala
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:sala_listar')
	
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar Sala"
		context['breadcrumb_link'] = "sala_listar"
		return super().get_context_data(**context)

# Fim do CRUD SALAS

# CRUD consumo

# class ConsumoListView(generic.ListView):
#     model = Consumo
#     template_name = 'gerenciamento/listar/consumo_listar.html'

# class ConsumoCreateView(generic.CreateView):
# 	model = Consumo
# 	template_name = 'gerenciamento/cadastrar.html'
# 	form_class = ConsumoForm
# 	success_url = reverse_lazy('sistema:consumo_listar')
	
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Cadastrar consumo"
# 		context['breadcrumb_title'] = "Consumo"
# 		context['breadcrumb_link'] = "consumo_listar"
# 		return super().get_context_data(**context)
# 	# Modificar field do formulário
# 	# def get_form(self, form_class=None):
# 	# 	form = super(ConsumoCreateView, self).get_form(form_class)
# 	# 	form.fields['data'].widget.attrs.update({'class': 'datepicker'})
# 	# 	return form

# class ConsumoUpdateView(generic.UpdateView):
# 	model = Consumo
# 	template_name = 'gerenciamento/editar.html'
# 	form_class = ConsumoForm
# 	success_url = reverse_lazy('sistema:consumo_listar')
	
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Editar Consumo"
# 		context['breadcrumb_link'] = "consumo_listar"
# 		return super().get_context_data(**context)


# class ConsumoDeleteView(generic.DeleteView):
# 	model = Consumo
# 	template_name = 'gerenciamento/deletar.html'
# 	success_url = reverse_lazy('sistema:consumo_listar')
	
# 	def get_context_data(self, **kwargs):
# 		context = {}
# 		context['title'] = "Deletar Consumo"
# 		return super().get_context_data(**context)

# Fim do CRUD consumo

# CRUD SALAS

class UserListView(generic.ListView):
    model = User
    template_name = 'gerenciamento/listar/user_listar.html'

class UserCreateView(FormView):
	form_class = UserCreationForm
	template_name = 'gerenciamento/cadastrar.html'

	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		raw_password = form.cleaned_data.get('password1')
		# user = authenticate(username=username, password=raw_password)
		# login(self.request, user)
		return redirect('sistema:user_listar')
    
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Cadastrar User"
		context['breadcrumb_title'] = "User"
		context['breadcrumb_link'] = "user_listar"
		return super().get_context_data(**context)

class UserUpdateView(generic.UpdateView):
	model = User
	template_name = 'gerenciamento/editar.html'
	fields = ['first_name', 'last_name', 'username', 'email']
	success_url = reverse_lazy('sistema:user_listar')
	
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Editar User"
		context['breadcrumb_link'] = "user_listar"
		return super().get_context_data(**context)

class UserDeleteView(generic.DeleteView):
	model = User
	template_name = 'gerenciamento/deletar.html'
	success_url = reverse_lazy('sistema:user_listar')
	
	def get_context_data(self, **kwargs):
		context = {}
		context['title'] = "Deletar User"
		return super().get_context_data(**context)

# Fim do CRUD SALAS

# Popular select sala
def load_salas(request):
    predio_id = request.GET.get('predio')
    salas = Sala.objects.filter(predio__pk=predio_id)
    return render(request, 'hr/salas_dropdown_list_options.html', {'salas': salas})

# Popular select predio
def load_predios(request):
    estabelecimento_id = request.GET.get('estabelecimento')
    predios = Predio.objects.filter(estabelecimento__pk=estabelecimento_id)
    return render(request, 'hr/predios_dropdown_list_options.html', {'predios': predios})

#Empreendimento REST API

class EstabelecimentoAPICreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Estabelecimento.objects.all()
	serializer_class = EstabelecimentoSerializer
	

	def perform_create(self, serializer):
		"""Save the post data when creating a new consumo."""
		serializer.save()

class EstabelecimentoAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Estabelecimento.objects.all()
	serializer_class = EstabelecimentoSerializer

#Prédio REST API

class PredioAPICreateView(generics.ListCreateAPIView):
	queryset = Predio.objects.all()
	serializer_class = PredioSerializer

	def perform_create(self, serializer):
		serializer.save()

class PredioAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Predio.objects.all()
	serializer_class = PredioSerializer

#Sala REST API

class SalaAPICreateView(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def perform_create(self, serializer):
        serializer.save()

class SalaAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Sala.objects.all()
	serializer_class = SalaSerializer

#Consumo REST API

# class ConsumoAPICreateView(generics.ListCreateAPIView):
#     queryset = Consumo.objects.all()
#     serializer_class = ConsumoSerializer

#     def perform_create(self, serializer):
#         serializer.save()

# class ConsumoAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Consumo.objects.all()
#     serializer_class = ConsumoSerializer

# class ConsumoDetalhado(APIView):
# 	# authentication_classes = (authentication.TokenAuthentication,)
#     # permission_classes = (permissions.IsAdminUser,)

# 	def get(self, request, format=None, *args, **kwargs):
# 		context = {}
# 		sala = Sala.objects.get(slug=self.kwargs['slug'])
# 		# # Gráfico de histórico de consumo mensal
# 		date = arrow.now()
# 		# Mês atual usado como referencia para obter meses anteriores
# 		month_conunting = date.replace(day=1)

# 		# Listando ultimos meses en relação ao atual
# 		months_list_name = []
# 		months_list_number = []
# 		month_dict = {get_month_name(int(month_conunting.strftime("%m"))) : sum(Consumo.kwh for Consumo in (Consumo.objects.filter(sala=sala, data__month=int(month_conunting.strftime("%m")))))}
# 		months_list_name.insert(0, get_month_name(int(month_conunting.strftime("%m"))) + "/" + month_conunting.strftime("%y")) 
# 		months_list_number.insert(0, int(month_conunting.strftime("%m")))
# 		for x in range(5):
# 			month = (month_conunting - timedelta(days=1)).replace(day=1)
# 			month_name = get_month_name(int(month.strftime("%m"))) + "/" + month.strftime("%y")
# 			months_list_name.insert(0, month_name)
# 			months_list_number.insert(0, int(month.strftime("%m")))
# 			consumo_mes = sum(Consumo.kwh for Consumo in (Consumo.objects.filter(sala=sala, data__month=int(month.strftime("%m")))))
# 			month_dict[month_name] = consumo_mes 
# 			month_conunting = month
# 		context['months_cons'] = month_dict
		
# 		# Listando consumo de salas ao longo dos meses
# 		sala_consumo = []
# 		for m in months_list_number:
# 			consumo_mes_anterior = sum(Consumo.kwh for Consumo in (Consumo.objects.filter(sala=sala,
# 			 	data__month=m)))
# 			sala_consumo.insert(0, consumo_mes_anterior)

# 		it = iter(sala_consumo)
# 		context['price_last_month'] = ((next(it) / 100) * 2)
# 		context['price_2last_month'] = ((next(it) / 100) * 2)
# 		context['price_3last_month'] = ((next(it) / 100) * 2)
# 		context['60_days'] = thirty_day_api(sala)
# 		return Response(context)


# # Geração de datas e consumos diários

# def thirty_day_api(sala):
# 	context = {}
	
# 	data_consumo = {}

# 	date = arrow.now()
# 	for day in range(1, 60):
# 		consumo = Consumo.objects.filter(sala=sala, data__date=date.datetime)
# 		# Baseado na largura do array de consumos é feito a soma dos consumos diários
# 		if len(consumo) > 1 :
# 			consumoTotal = 0
# 			for consumos in consumo:
# 				consumoTotal += consumos.kwh
# 			final_data_consumo = consumoTotal
# 		elif len(consumo) == 1:
# 			final_data_consumo = consumo[0].kwh
# 		# Caso não tenha ocorrido nenhum consumo naquela data 0 será salvo no array de consumos
# 		else:
# 			final_data_consumo = 0
# 		data_consumo[str(date.datetime.date())] = final_data_consumo
# 		date = date.replace(days=-1)
# 	context["date_cons"] = data_consumo
# 	return context

# def thirty_day(sala):
# 	context = {}
	
# 	final_data = []
# 	final_data_consumo = []
# 	date = arrow.now()
# 	for day in range(1, 60):
# 		consumo = Consumo.objects.filter(sala=sala, data__date=date.datetime)
# 		# Baseado na largura do array de consumos é feito a soma dos consumos diários
# 		if len(consumo) > 1 :
# 			consumoTotal = 0
# 			for consumos in consumo:
# 				consumoTotal += consumos.kwh
# 			final_data_consumo.insert(0, consumoTotal)
# 		elif len(consumo) == 1:
# 			final_data_consumo.insert(0, consumo[0].kwh)
# 		# Caso não tenha ocorrido nenhum consumo naquela data 0 será salvo no array de consumos
# 		else:
# 			final_data_consumo.insert(0, 0)
# 		data = date.datetime.date()
# 		final_data.insert(0, data)
# 		date = date.replace(days=-1)
# 	context['final_data'] = final_data
# 	context['final_data_consumo'] = final_data_consumo
# 	return context

# def get_month_name(month_no):
# 	with different_locale('pt-br'):
# 		return month_name[month_no]