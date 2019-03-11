from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import *
from .forms import *
from django import forms
from datetime import date, datetime, timedelta
import calendar
# Rest and Serializers
from rest_framework import generics
from .serializers import *
# User Create 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import DetailView
import arrow
from django.core.exceptions import ObjectDoesNotExist


class IndexListView(generic.TemplateView):
	template_name = 'sistema/index.html'

class ChartListView(generic.TemplateView):
	template_name = 'sistema/chart.html'
	def authenticated(self, user):
		return self.filter(user=user)
	def get_context_data(self, **kwargs):
		context = {}
		if self.request.user.username == "admin": 
			context['salas'] = Sala.objects.all()
		else: 
			context['salas'] = Sala.objects.filter(estabelecimento__user__username=self.request.user)
		return super().get_context_data(**context)
	def post(self, request):
		context = {}
		if self.request.user.username == "admin":
			context['salas'] = Sala.objects.all()
		else: 
			context['salas'] = Sala.objects.filter(estabelecimento__user__username=self.request.user)
		context['select_sala'] = request.POST['select_sala']
		context['sala'] = Sala.objects.get(slug=context['select_sala'])
		# Gráfico de histórico de consumo mensal
		month_before = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1)
		
		meses = {calendar.month_name[int(month_before.strftime("%m"))] : month_before} 
		for x in range(2,7):
			month = (month_before - timedelta(days=1)).replace(day=1)
			mes_name = calendar.month_name[int(month.strftime("%m"))]
			meses[mes_name] = month
			month_before = month			
		context['meses'] = meses
		
		sala_consumo = []
		for x, y in meses.items():
			consumo_mes_anterior = sum(Consumo.kwh for Consumo in 
				(Consumo.objects.filter(sala=context['sala'], data__month=y.strftime("%m"))))
			sala_consumo.append(consumo_mes_anterior)	

		context['sala_consumo'] = sala_consumo
		it = iter(sala_consumo)
		context['preco_last_month'] = (next(it) / 100) * 2
		context['preco_2last_month'] = (next(it) / 100) * 2
		context['preco_3last_month'] = (next(it) / 100) * 2
		context['30_days'] = self.thirty_day(context['sala'])
		return render(request, self.template_name, context)
	def thirty_day(self, sala, **kwargs):
		context = {}
		
		final_data = []
		final_data_consumo = []

		date = arrow.now()
		for day in range(1, 60):
			try:
				consumos = Consumo.objects.get(sala=sala, data=date.datetime)
				final_data_consumo.insert(0, consumos.kwh)
			except ObjectDoesNotExist:
				consumos = 0
				final_data_consumo.insert(0, consumos)
			data = date.datetime
			final_data.insert(0, data)
			date = date.replace(days=-1)
		context['final_data'] = final_data
		context['final_data_consumo'] = final_data_consumo
		return context

# CRUD Estabelecimento

class EstabelecimentoListView(generic.ListView):
    model = Estabelecimento
    template_name = 'gerenciamento/listar/estabelecimento_listar.html'

class EstabelecimentoCreateView(generic.CreateView):
	model = Estabelecimento
	template_name = 'gerenciamento/cadastrar.html'
	fields = ['nome', 'user']
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
		context['breadcrumb_link'] = "consumo_listar"
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


#Consumo REST API

class ConsumoAPICreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ConsumoAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer

#Sala REST API

class SalaAPICreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class SalaAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Sala.objects.all()
	serializer_class = SalaSerializer
