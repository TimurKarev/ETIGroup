from django.forms import ModelForm

from otk.models.checklists import *

class SubstationTypePointForm(ModelForm):
    class Meta:
        model = SubstationTypePoint
        fields = ['choise']