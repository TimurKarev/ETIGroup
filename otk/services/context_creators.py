from typing import Optional

from otk.models.checklists import *
from otk.services.order_services import get_section_context


def get_detail_context_from_checklist_object(checklist_object, post_data=None) -> Optional[list]:
    """Возвращает список сущностей для присоединения к context в DetailView
        для конкретного чеклиста"""
    sections = checklist_object.chlistsection_set.all()
    data = []
    for i, section in enumerate(sections):
        data.append(get_section_context(section, data=post_data, section_prefix='sec' + str(i)))

        # sec_dict = {'name': section.name}
        #
        # str_dict = {}
        # string_points = section.stringpoint_set.all()
        # for str_count, string_point in enumerate(string_points):
        #     str_list = [
        #         string_point.name,
        #         string_point.string,
        #         ]
        #     str_dict['string_point' + str(str_count)] = str_list
        # sec_dict['string_points'] = str_dict
        #
        # fp_dict = {}
        # fourchoisepoints = section.fourchoisepoint_set.all()
        # for fp_count, fourchoisepoint in enumerate(fourchoisepoints):
        #     fp_list = [fourchoisepoint.name,
        #             fourchoisepoint.choice,
        #             fourchoisepoint.comment]
        #     fp_dict['four_point' + str(fp_count)] = fp_list
        # sec_dict['four_points'] = fp_dict
        #
        # yes_no = section.yesnochoicepoint_set.all()[0]
        # sec_dict['yes_no'] = {'name': yes_no.name,
        #                     'choice': yes_no.choice}
        # data.append(sec_dict)

    return data


from django.forms.models import inlineformset_factory

'''Возвращает список сущностей для присоединения к context в UpdateView 
    для конкретного чеклиста'''


def get_update_context_from_checklist_object(checklist_object, post=None) -> Optional[list]:
    FourChoisePointFormset = inlineformset_factory(
        ChListSection, FourChoicePoint, form=FourChoisePointForm, extra=0,
    )

    StringPointFormset = inlineformset_factory(
        ChListSection, StringPoint, fields=['string'], extra=0,
    )

    data = []
    sections = checklist_object.chlistsection_set.all()
    for num, section in enumerate(sections):
        sec_dict = {'name': section.name}

        sec_dict['string_forms'] = StringPointFormset(post, instance=section, prefix='id_str' + str(num))
        stringpoints = section.stringpoint_set.all()
        str_names = []
        for _, stringpoint in enumerate(stringpoints):
            str_names.append(stringpoint.name)
        sec_dict['string_names'] = str_names

        sec_dict['four_forms'] = FourChoisePointFormset(post, instance=section, prefix='id_sec' + str(num))
        fourchoisepoints = section.fourchoisepoint_set.all()
        fp_names = []
        for _, fourchoisepoint in enumerate(fourchoisepoints):
            fp_names.append(fourchoisepoint.name)
        sec_dict['four_names'] = fp_names

        data.append(sec_dict)

    return data


'''Сохраняет все формсеты'''


def save_all_formsets(context, object):
    inst_list = object.chlistsection_set.all()
    for i, inst in enumerate(inst_list):
        formset = context["sections"][i]['string_forms']
        _save_formset(formset, inst)

    for i, inst in enumerate(inst_list):
        formset = context["sections"][i]['four_forms']
        _save_formset(formset, inst)


'''Сохраняет один формсет'''


def _save_formset(formset, inst):
    if formset.is_valid():
        formset.instance = inst
        formset.save()
    else:
        print(formset.errors)
