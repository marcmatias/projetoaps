from django.contrib import admin
from . models import Predio, Sala, Consumo

# Register your models here.

# admin.site.register(Estabelecimento)
admin.site.register(Predio)
admin.site.register(Sala)
admin.site.register(Consumo)
