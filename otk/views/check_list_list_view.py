import json

from django.urls import reverse

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
                'order_id': order.id,
                'order_num': {
                    'name': int(order.man_number),
                    'link': reverse('order_detail', kwargs={'pk': order.id}),
                },
                'build': self.get_checklist_frontend_data(order, 'bm_checklist'),
                'tm': self.get_checklist_frontend_data(order,  'tm_checklist'),
                'el': self.get_checklist_frontend_data(order, 'el_checklist'),
                'doc': self.get_checklist_frontend_data(order, 'doc_checklist'),
                'zip': self.get_checklist_frontend_data(order, 'zip_checklist'),
                'sal': self.get_checklist_frontend_data(order, 'sal_checklist'),
            })

        json_data = json.dumps(order_list)
        return {'gj_checklists_list': json_data}

    def is_checklist_available(self, checklist):
        if checklist:
            return True
        else:
            return False

    def get_checklist_frontend_data(self, order, checklist_name):
        data = {}
        if not getattr(order, checklist_name):
            data['name'] = 'создать'
            data['link'] = reverse('checklist_create', kwargs={'tp': checklist_name, 'pk': order.id})
        else:
            checklist = getattr(order, checklist_name)
            print(checklist, checklist.id, reverse('checklist_detail', kwargs={'tp': checklist_name, 'pk': int(checklist.id)}))
            data['name'] = 'просмотр'
            data['link'] = reverse('checklist_detail', kwargs={'tp': checklist_name, 'pk': int(checklist.id)})
        return data

