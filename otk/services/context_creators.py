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

###########
    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     print('#####################################form_valid', form)
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     print('#####################################form_valid', form)
    #     return super().form_valid(form)
#############


'''Возвращает список сущностей для присоединения к context в UpdateView 
    для конкретного чеклиста'''
def get_update_context_from_checklist_object(checklist_object) -> Optional[list]:
    sections = checklist_object.chlistsection_set.all()
    data = []
    for _, section in enumerate(sections):
        sec_dict = {'name': section.name}
        fp_dict = {}
        fourchoisepoints = section.fourchoisepoint_set.all()
        for fp_count, fourchoisepoint in enumerate(fourchoisepoints):
            fp_list = [fourchoisepoint.name, 
                        FourChoisePointForm(instance = fourchoisepoint)]
            fp_dict['four_point' + str(fp_count)] = fp_list
        sec_dict['four_point'] = fp_dict
        yes_no = section.yesnochoisepoint_set.all()[0]
        sec_dict['yes_no'] = {'name': yes_no.name,
                            'choise': yes_no.choise}
        data.append(sec_dict)

    return data