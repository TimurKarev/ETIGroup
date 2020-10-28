from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from otk.models.order import OTKOrder


# Create your views here.
class CheckListListView(ListView):
    model = OTKOrder
    template_name = 'checklist_list.html'
    
    def get_queryset(self):
        if self.request.GET.get('print_btn'):
            print ("Click")
        print ("TYTUYYUYUYTUYU")
        return super().get_queryset()

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