from django import forms

class CreateTMChecklistForm(forms.Form):
    RM6_number_form = forms.IntegerField(label="Количество RM6")

class UpdateTMChecklistForm(forms.Form):
    radio = forms.ChoiceField(choices=[('0', 'В работе'),('1', "Готово"), ('2', 'НЕ принято')], label = 'Радио кнопка')
    pass