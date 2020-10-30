from django.views.generic.edit import FormView, UpdateView

from otk.views.forms.tm_checklist_forms import *

from otk.models.order import OTKOrder
from otk.models.order import TMCheckList

class TMCheckListCreateView(FormView):
    template_name = 'tm_checklist_create.html'
    form_class = CreateTMChecklistForm
    success_url = '/'
    
    def get_initial(self):
        initial = super(TMCheckListCreateView, self).get_initial()
            
        initial.update({'RM6_number_form': 4})
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['man_number'] = OTKOrder.objects.get(id = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        print(form.cleaned_data)
        self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
        
        #TODO create factory
        '''
        ###############################
        '''

        try:
            tm_checklist = TMCheckList(UE_Code = ' ', TM_Code = ' ', Type_KTM_UE = ' ', Number_KTM_UE = ' ')
            tm_checklist.save()
        except:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print('Error  - tm_checklist.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            order = OTKOrder.objects.get(id = self.kwargs['pk'])
            order.tm_checklist =  tm_checklist
            order.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'Error  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)
        '''
        ###############################
        '''
        
        self.success_url = '/tm_checklist_update/' + str(self.kwargs['pk'])
        return super(TMCheckListCreateView, self).form_valid(form)
    

class TMCheckListUpdateView(UpdateView):
    model = OTKOrder
    #form_class = UpdateTMChecklistForm
    template_name = "tm_checklist_update.html"
    fields = '__all__'