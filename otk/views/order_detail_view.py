from otk.services.services import get_section_context
from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.otk_order import OTKOrder

from django.views.generic import TemplateView


class OrderDetailView(UserAccessMixin, TemplateView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = {}
        order = OTKOrder.objects.get(id=kwargs['pk'])
        context['order_number'] = order.man_number
        context['order_pk'] = order.id
        context['subst_type'] = order.config_section.substationtypepoint_set.all()[0].point_value
        context['config'] = get_section_context(order.config_section)

        return context
