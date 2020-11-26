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
        fields = ['point_value']


class StringPointForm(ModelForm):
    class Meta:
        model = StringPoint
        fields = ['point_value']


class IntegerPointForm(ModelForm):
    class Meta:
        model = IntegerPoint
        fields = ['point_value']

    def is_valid(self):
        super().is_valid()
        print(self.instance)
        print(self.cleaned_data)



class FourChoicePointForm(ModelForm):
    class Meta:
        model = FourChoicePoint
        fields = ['point_value', 'comment']
