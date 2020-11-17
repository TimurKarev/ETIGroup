from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import DetailView

from otk.models.checklists import *

class CheckListDetailView(UserAccessMixin, DetailView):
    permission_required = 'otk.view_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'
    
    model = Checklist
    template_name = "checklist_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(CheckListDetailView, self).get_context_data(**kwargs)

        sections = self.object.chlistsection_set.all()
        data = []
        for sec_count, section in enumerate(sections):
            sec_dict = {'name': section.name}
            fp_dict = {}
            fourchoisepoints = section.fourchoisepoint_set.all()
            for fp_count, fourchoisepoint in enumerate(fourchoisepoints):
                fp_list = [fourchoisepoint.name, 
                           fourchoisepoint.choise,
                           fourchoisepoint.comment]
                fp_dict['four_point'] = fp_list
            sec_dict['four_point'] = fp_dict
            yes_no = section.yesnochoisepoint_set.all()[0]
            sec_dict['yes_no'] = {'name': yes_no.name,
                                  'choise': yes_no.choise}
            data.append(sec_dict)
        print(data)
        context['data'] = data
            #d['section_1' + str(sec_count)]
        return context