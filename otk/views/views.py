from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.views.generic import ListView
from otk.models.otk_order import OTKOrder


# Create your views here.
class CheckListListView(UserAccessMixin, ListView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'login'
    
    model = OTKOrder
    template_name = 'checklist_list.html'
