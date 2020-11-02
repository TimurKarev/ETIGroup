from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView

from otk.views.forms.tm_checklist_forms import *

from otk.models.order import OTKOrder
from otk.models.order import TMCheckList
from otk.models.order import RM6CheckList
from otk.models.order import OneMoreTables

from django.urls import reverse

from django.forms.models import inlineformset_factory

ChildFormset = inlineformset_factory(
    TMCheckList, RM6CheckList, fields=('serial',), extra = 0,
)

MoreFormset = inlineformset_factory(
    TMCheckList, OneMoreTables, fields=('serial',), extra = 0,
)

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
        print(form.cleaned_data['RM6_number_form'])
        rm_number = form.cleaned_data['RM6_number_form']
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
            for _ in range(rm_number):
                rm6_checklist = RM6CheckList(checklist = tm_checklist, serial = '')
                rm6_checklist.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'Error  - order.save()')
            return super(TMCheckListCreateView, self).form_valid(form)

        try:
            one_more = OneMoreTables(checklist = tm_checklist, serial = '')
            one_more.save()
        except Exception as e:
            self.success_url = '/tm_checklist_create/' + str(self.kwargs['pk'])
            print(e + 'Error  - order.save()')
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
        
        self.success_url = '/tm_checklist_update/' + str(tm_checklist.id)
        return super(TMCheckListCreateView, self).form_valid(form)
    


class TMCheckListUpdateView(UpdateView):
    model = TMCheckList
    #form_class = UpdateTMChecklistForm
    template_name = "tm_checklist_update.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["children"] = ChildFormset(self.request.POST, instance=self.object)
            data["one"] = MoreFormset(self.request.POST, instance=self.object)
        else:
            data["children"] = ChildFormset(instance=self.object)
            data["one"] = MoreFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children = context["children"]
        self.object = form.save()
        if children.is_valid():
            children.instance = self.object
            children.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('/tm_checklist_detail/' + str(tm_checklist.id))

from django.core import serializers
from django.forms.models import model_to_dict
from otk.utils import model_to_dict_verbose

class TMCheckListDetailView(DetailView):
    model = TMCheckList
    template_name = "tm_checklist_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(TMCheckListDetailView, self).get_context_data(**kwargs)

        context['chlist_dict'] = model_to_dict_verbose(self.object, exclude=['id'])
        
        context['rm6s'] = {}
        rm6s = self.object.rm6checklist_set.all()
        for i in range(len(rm6s)):
            rm = {}
            rm["rm6-"] = ' '
            rm.update(model_to_dict_verbose(rm6s[i], exclude=['id', 'checklist']))
            print(rm)
            rm = {str(key) + '(' + str(i+1) + ')' : val for key, val in rm.items()}
            print(rm)
            context['rm6s'].update(rm)
        # print(model_to_dict_verbose(rm6s[0], exclude=['id']), len(rm6s))
        # context['rm6s'] = self.object.rm6checklist_set.all()

        return context