from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

app_name = 'sistema'

urlpatterns = [
	# path('admin/', admin.site.urls),
	# path('', login_required(views.IndexListView.as_view(), login_url=reverse_lazy('sistema:login')), name='index'),
	path('', login_required(views.IndexListView.as_view()), name="home"),
	# Predio urls
	path('predio_listar/', login_required(views.PredioListView.as_view()), name="predio_listar"),
	path('predio_cadastrar/', login_required(views.PredioCreateView.as_view()), name="predio_cadastrar"),
	path('predio_editar_form/<slug:slug>', login_required(views.PredioUpdateView.as_view()), name="predio_editar"),
	path('predio_deletar_form/<slug:slug>', login_required(views.PredioDeleteView.as_view()), name="predio_deletar"),
	# Estabelecimento urls
	path('estabelecimento_listar/', login_required(views.EstabelecimentoListView.as_view()), name="estabelecimento_listar"),
	path('estabelecimento_cadastrar/', login_required(views.EstabelecimentoCreateView.as_view()), name="estabelecimento_cadastrar"),
	path('estabelecimento_editar_form/<slug:slug>', login_required(views.EstabelecimentoUpdateView.as_view()), name="estabelecimento_editar"),
	path('estabelecimento_deletar_form/<slug:slug>', login_required(views.EstabelecimentoDeleteView.as_view()), name="estabelecimento_deletar"),
	# Estabelecimento urls
	path('sala_listar/', login_required(views.SalaListView.as_view()), name="sala_listar"),
	path('sala_cadastrar/', login_required(views.SalaCreateView.as_view()), name="sala_cadastrar"),
	path('sala_editar_form/<slug:slug>', login_required(views.SalaUpdateView.as_view()), name="sala_editar"),
	path('sala_deletar_form/<slug:slug>', login_required(views.SalaDeleteView.as_view()), name="sala_deletar"),
	# Estabelecimento urls
	path('consumo_listar/', login_required(views.ConsumoListView.as_view()), name="consumo_listar"),
	path('consumo_cadastrar/', login_required(views.ConsumoCreateView.as_view()), name="consumo_cadastrar"),
	path('consumo_editar_form/<slug:slug>', login_required(views.ConsumoUpdateView.as_view()), name="consumo_editar"),
	path('consumo_deletar_form/<slug:slug>', login_required(views.ConsumoDeleteView.as_view()), name="consumo_deletar"),

	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, {'next_page': reverse_lazy('sistema:login')}, name='logout'),
]
