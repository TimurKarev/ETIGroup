from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.services.services import create_checklist_from_json

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from otk.models.otk_order import OTKOrder


class OrderConfigCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'order_config_create.html'

    order_checklist_type = 'order_config'

    def get(self, request, *args, **kwargs):
        # order = OTKOrder.objects.get(id=int(kwargs['pk']))
        print('OrderConfigCreateView', kwargs)

        # checklist_name = "Электрическая часть заказ №" + str(order.man_number)

        # checklist_id = create_checklist_from_json(
        #     order,
        #     self.el_checklist_type,
        #     checklist_name
        # )

        # if checklist_id is not None:
        #     return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': checklist_id}))
        # else:
        return HttpResponse('Мы на нужной странице')
