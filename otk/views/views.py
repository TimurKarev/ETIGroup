from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from otk.models.order import OTKOrder


# Create your views here.
class CheckListListView(ListView):
    model = OTKOrder
    template_name = 'checklist_list.html'
    
    def get(self, request):
        
        if request.GET.get('print_btn'):
            #OTKOrder(man_number = '1555', )
            print ("Click")
        print ("kasladfk;dk;lasdk;LASDK;LASKD;LASKD;Laskds;ladsad;lk")
        return HttpResponseRedirect('')

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