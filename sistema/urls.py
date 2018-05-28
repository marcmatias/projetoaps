from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

app_name = 'sistema'

urlpatterns = [
	# path('admin/', admin.site.urls),
	# path('', login_required(views.IndexListView.as_view(), login_url=reverse_lazy('sistema:login')), name='index'),

	path('', views.IndexListView.as_view(), name="home"),
	# Predio urls
	path('predio_listar/', views.PredioListView.as_view(), name="predio_listar"),
	path('predio_cadastrar/', views.PredioCreateView.as_view(), name="predio_cadastrar"),
	path('predio_editar_form/<slug:slug>', views.PredioUpdateView.as_view(), name="predio_editar"),
	path('predio_deletar_form/<int:pk>,<slug:slug>', views.PredioDeleteView.as_view(), name="predio_deletar"),
	# Estabelecimento urls
	path('estabelecimento_listar/', views.EstabelecimentoListView.as_view(), name="estabelecimento_listar"),
	path('estabelecimento_cadastrar/', views.EstabelecimentoCreateView.as_view(), name="estabelecimento_cadastrar"),
	path('estabelecimento_editar_form/<slug:slug>', views.EstabelecimentoUpdateView.as_view(), name="estabelecimento_editar"),
	path('estabelecimento_deletar_form/<slug:slug>', views.EstabelecimentoDeleteView.as_view(), name="estabelecimento_deletar"),


	    # path('login/', auth_views.login, {'template_name': 'sistema/login.html'}, name='login'),
	    # path('logout/', auth_views.logout, {'next_page': reverse_lazy('sistema:index')}, name='logout'),
]
