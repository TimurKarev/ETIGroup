from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.otk_order import OTKOrder

from django.views.generic import  DetailView

class OrderDetailView(UserAccessMixin, DetailView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'checklist_list'
    
    model = OTKOrder
    template_name = 'order_detail.html'
    fields = ['man_number', 'substation_type', 'rm_number', 'ybp_number', 'su_number']