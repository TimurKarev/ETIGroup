from typing import Optional

from otk.models.checklists import *


'''Возвращает список сущностей для присоединения к context в DetailView 
    для конкретного чеклиста'''
def get_detail_context_from_checklist_object(checklist_object) -> Optional[list]:
    sections = checklist_object.chlistsection_set.all()
    data = []
    for _, section in enumerate(sections):
        sec_dict = {'name': section.name}
        fp_dict = {}
        fourchoisepoints = section.fourchoisepoint_set.all()
        for fp_count, fourchoisepoint in enumerate(fourchoisepoints):
            fp_list = [fourchoisepoint.name, 
                    fourchoisepoint.choise,
                    fourchoisepoint.comment]
            fp_dict['four_point' + str(fp_count)] = fp_list
        sec_dict['four_point'] = fp_dict
        yes_no = section.yesnochoisepoint_set.all()[0]
        sec_dict['yes_no'] = {'name': yes_no.name,
                            'choise': yes_no.choise}
        data.append(sec_dict)

    return data

from django.forms.models import inlineformset_factory
from django import forms

class FourChoisePointForm(forms.ModelForm):
    class Meta:
        model = FourChoisePoint
        fields = ['choise', 'comment']

'''Возвращает список сущностей для присоединения к context в UpdateView 
    для конкретного чеклиста'''
def get_update_context_from_checklist_object(checklist_object, post=None) -> Optional[list]:
    
    FourChoisePointFormset = inlineformset_factory(
        ChListSection, FourChoisePoint, form = FourChoisePointForm, extra = 0,
)
    sections = checklist_object.chlistsection_set.all()
    data = []
    for num, section in enumerate(sections):
        sec_dict = {'name': section.name}
        sec_dict['four_forms'] = FourChoisePointFormset(post, instance=section, prefix = 'id_sec'+ str(num))
        fourchoisepoints = section.fourchoisepoint_set.all()
        fp_names = []
        for _, fourchoisepoint in enumerate(fourchoisepoints):
            fp_names.append(fourchoisepoint.name)
        sec_dict['four_names'] = fp_names
        data.append(sec_dict)

    return data