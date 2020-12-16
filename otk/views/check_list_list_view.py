import json

from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.views.generic import TemplateView
from otk.models.otk_order import OTKOrder


# Create your views here.
class CheckListListView(UserAccessMixin, TemplateView):
    permission_required = 'otk.view_order'
    redirect_without_permission = 'login'

    template_name = 'checklist_list.html'

    def get_context_data(self, **kwargs):
        orders = OTKOrder.objects.all()

        order_list = []
        for order in orders:
            order_list.append({
                'order_num': order.man_number,
                'order_id': order.id,
                'build': str(order.bm_checklist),
                'tm': str(order.tm_checklist),
                # 'el': order.el_checklist,
                # 'doc': order.doc_checklist,
                # 'zip': order.zip_checklist,
                # 'sal': order.sal_checklist,
            })

        json_data = json.dumps(order_list)
        return {'gj_checklists_list': json_data}
