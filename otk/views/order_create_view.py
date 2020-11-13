from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.order import OTKOrder

from django.views.generic import  CreateView

class OrderCreateView(UserAccessMixin, CreateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'
    
    model = OTKOrder
    template_name = 'order_create.html'
    fields = ['man_number', 'substation_type', 'rm_number', 'ybp_number', 'su_number']

    # def form_valid(self, form):
    #     form.save()
    #     return super(OrderCreateView, self).form_valid(form)