from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from otk.models.order import OTKOrder
from otk.models.tm_checklists import TMCheckList


# Create your views here.
class CheckListListView(ListView):
    model = OTKOrder
    template_name = 'checklist_list.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super(CheckListListView, self).get_context_data(**kwargs)
    #     tm_check_exist = None
    #     try:
    #         self.model._meta.get_field('tm_checklist')
    #     except:
    #         pass
    #     context['tm_check_exist'] = tm_check_exist
    #     return context
    
    # def get_queryset(self):
    #     if self.request.GET.get('print_btn'):
    #         print ("Click")
    #         tm_chlst = TMCheckList()
    #         tm_chlst.save()
    #         order = OTKOrder(1555, tm_chlst)
    #         order.save()
                
    #     print ("TYTUYYUYUYTUYU")
    #     return super().get_queryset()

# class CkeckListDetailView(DetailView):
#     model = TMCheckList
#     template_name = 'checklist_detail.html'
    
# class CheckListListCreate(CreateView):
#     model = TMCheckList
#     template_name = 'checklist_new.html'
#     fields = '__all__'

# class CheckListListEdit(UpdateView):
#     model = TMCheckList
#     template_name = 'checklist_edit.html'
#     fields = '__all__'