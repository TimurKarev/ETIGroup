from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from otk.models.order import OTKOrder
from otk.models.tm_checklists import TMCheckList


# Create your views here.
class CheckListListView(UserAccessMixin, ListView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'login'
    
    model = OTKOrder
    template_name = 'checklist_list.html'
    

class OrderCreateView(UserAccessMixin, CreateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'
    
    model = OTKOrder
    template_name = 'order_create.html'
    success_url = '/'
    fields = ['man_number']