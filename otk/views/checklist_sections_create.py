from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.generic import RedirectView
from otk.models.otk_order import OTKOrder
from otk.services.services import get_checklist_name_by_type, create_checklist_by_checklist_type_from_json


class CheckListSectionsCreateView(RedirectView):

    def get(self, request, *args, **kwargs):
        # print(request, args, kwargs)

        order_entry = OTKOrder.objects.get(id=int(kwargs['pk']))
        checklist_name = get_checklist_name_by_type(kwargs['tp'], order_entry.man_number)

        checklist_id = create_checklist_by_checklist_type_from_json(
            order_entry,
            kwargs['tp'],
            checklist_name
        )

        if checklist_id is not None:
            return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': checklist_id}))
        else:
            return HttpResponse('Ошибка при создании чек листа')
