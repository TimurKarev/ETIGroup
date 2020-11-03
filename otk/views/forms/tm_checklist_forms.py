from django import forms

class CreateTMChecklistForm(forms.Form):
    RM6_number_form = forms.IntegerField(label="Количество RM6")
    YBP_number_form = forms.IntegerField(label="Количество УВР")
    SU_number_form = forms.IntegerField(label="Количество ШУ")
