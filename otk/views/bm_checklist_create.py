from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.services.services import create_checklist_from_json

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from pathlib import Path
import os

from otk.models.otk_order import OTKOrder

class BMCheckListCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'bm_checklist_create.html'

    bm_checklist_type = 'bm_checklist'


    def get(self, request, *args, **kwargs):
        order = OTKOrder.objects.get(id=int(kwargs['pk']))

        checklist_name = "Строительная часть заказ №" + str(order.man_number)

        # BASE_DIR = Path(__file__).resolve().parent.parent.parent
        # JSON_DIR = Path('static/json/bm_checklist.json')
        # path = os.path.join(BASE_DIR, JSON_DIR)

        
        bm_checklist_id = create_checklist_from_json(
                                                order,
                                                self.bm_checklist_type,
                                                checklist_name
                                                )

        if bm_checklist_id is not None:
            return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': bm_checklist_id}))
        else:
            return HttpResponse('Ошибка при создании чек листа')