from django import forms
from .models import *


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('estabelecimento', 'predio', 'nome')
    # Função para funcionalmento de select ajax Predio e Sala
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Predio
        self.fields['predio'].queryset = Predio.objects.none()

        if 'estabelecimento' in self.data:
            try:
                estabelecimento_id = int(self.data.get('estabelecimento'))
                self.fields['predio'].queryset = Predio.objects.filter(estabelecimento_id=estabelecimento_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Predio queryset
        elif self.instance.pk:
            self.fields['predio'].queryset = self.instance.estabelecimento.predio_set.order_by('nome')

class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = ('estabelecimento', 'predio', 'sala', 'kwh', 'data')
    # Função para funcionalmento de select ajax Predio e Sala
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['readonly'] = True
        # Sala
        self.fields['sala'].queryset = Sala.objects.none()
        
        if 'predio' in self.data:
            try:
                predio_id = int(self.data.get('predio'))
                self.fields['sala'].queryset = Sala.objects.filter(predio_id=predio_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Sala queryset
        elif self.instance.pk:
            self.fields['sala'].queryset = self.instance.predio.sala_set.order_by('nome')
        # Predio
        self.fields['predio'].queryset = Predio.objects.none()

        if 'estabelecimento' in self.data:
            try:
                estabelecimento_id = int(self.data.get('estabelecimento'))
                self.fields['predio'].queryset = Predio.objects.filter(estabelecimento_id=estabelecimento_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Predio queryset
        elif self.instance.pk:
            self.fields['predio'].queryset = self.instance.estabelecimento.predio_set.order_by('nome')