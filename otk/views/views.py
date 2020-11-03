from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from otk.models.order import OTKOrder
from otk.models.tm_checklists import TMCheckList


# Create your views here.
class CheckListListView(ListView):
    model = OTKOrder
    template_name = 'checklist_list.html'
    

class OrderCreateView(CreateView):
    model = OTKOrder
    template_name = 'order_create.html'
    success_url = '/'
    fields = ['man_number']