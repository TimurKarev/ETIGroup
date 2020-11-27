from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.services.services import create_checklist_by_checklist_type_from_json

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from otk.models.otk_order import OTKOrder


class TMCheckListCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'tm_checklist_create.html'

    el_checklist_type = 'tm_checklist'

    def get(self, request, *args, **kwargs):
        order = OTKOrder.objects.get(id=int(kwargs['pk']))

        checklist_name = "Чек лист телемеханики, заказ №" + str(order.man_number)

        checklist_id = create_checklist_by_checklist_type_from_json(
            order,
            self.el_checklist_type,
            checklist_name
        )

        if checklist_id is not None:
            return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': checklist_id}))
        else:
            return HttpResponse('Ошибка при создании чек листа')