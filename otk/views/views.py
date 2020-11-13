from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView
from otk.models.order import OTKOrder
from otk.models.tm_checklists import TMCheckList


# Create your views here.
class CheckListListView(UserAccessMixin, ListView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'login'
    
    model = OTKOrder
    template_name = 'checklist_list.html'
    
