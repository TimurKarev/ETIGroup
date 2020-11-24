from django.forms import ModelForm
from otk.models.otk_order import OTKOrder
from otk.models.checklists import *


class OTKOrderForm(ModelForm):
    class Meta:
        model = OTKOrder
        fields = ['man_number']


class SubstationTypePointForm(ModelForm):
    class Meta:
        model = SubstationTypePoint
        fields = ['choice']
