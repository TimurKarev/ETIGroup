from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.views.generic.edit import FormView

from otk.views.forms.tm_checklist_forms import CreateTMChecklistForm

from otk.models.order import OTKOrder
from otk.models.tm_checklists import *

from django.urls import reverse

from otk.utils import model_to_dict_verbose

from django.forms.models import inlineformset_factory

class TMCheckListCreateView(UserAccessMixin, FormView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'
    
    template_name = 'tm_checklist_create.html'
    form_class = CreateTMChecklistForm
    success_url = '/'
    
    def get_initial(self):
        initial = super(TMCheckListCreateView, self).get_initial()

        #TODO: сделать конфигуратор для значений по умолчанию
        initial.update({'RM6_number_form': 4,
                        'YBP_number_form': 2,
                        'SU_number_form': 2,
                        })
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['man_number'] = OTKOrder.objects.get(id = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        rm_number = form.cleaned_data['RM6_number_form']
        ybp_number = form.cleaned_data['YBP_number_form']
        su_number = form.cleaned_data['SU_number_form']
            
        self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
        
        #TODO create factory
        '''
        ###############################
        '''
        try:
            tm_checklist = TMCheckList()
            tm_checklist.save()
        except:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print('Error  - tm_checklist.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            tm_srtm = SRTMCheckList(checklist = tm_checklist)
            tm_srtm.save()
        except:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print('Error  - SRtm save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            tm_sktm = SKTMCheckList(checklist = tm_checklist)
            tm_sktm.save()
        except:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print('Error  - SKTM save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            tm_ktmue = KTMUECheckList(checklist = tm_checklist)
            tm_ktmue.save()
        except:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print('Error KTMUECheckList -  save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            for _ in range(rm_number):
                rm6_checklist = RM6CheckList(checklist = tm_checklist)
                rm6_checklist.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'Error  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            for _ in range(ybp_number):
                ybp_checklist = YBPCheckList(checklist = tm_checklist)
                ybp_checklist.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'YBP  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            for _ in range(su_number):
                su_checklist = SUCheckList(checklist = tm_checklist)
                su_checklist.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'SU  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            order = OTKOrder.objects.get(id = self.kwargs['pk'])
            order.tm_checklist = tm_checklist
            order.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'Error  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)
        '''
        ###############################
        '''
        
        self.success_url = '/tm_checklist_update/' + str(tm_checklist.id)
        return super(TMCheckListCreateView, self).form_valid(form)
    