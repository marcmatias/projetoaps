from django import forms
from .models import *


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('predio', 'nome')

class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = ('predio', 'sala', 'kwh', 'data')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sala'].queryset = Sala.objects.none()

        if 'predio' in self.data:
            try:
                predio_id = int(self.data.get('predio'))
                self.fields['sala'].queryset = Sala.objects.filter(predio_id=predio_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sala'].queryset = self.instance.predio.sala_set.order_by('nome')
