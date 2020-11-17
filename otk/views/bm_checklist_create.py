from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.services.services import create_bmchecklist_from_json

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from otk.models.order import OTKOrder

class BMCheckListCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'bm_checklist_create.html'


    def get(self, request, *args, **kwargs):
        order = OTKOrder.objects.get(id=int(kwargs['pk']))
        bm_checklist_id = create_bmchecklist_from_json(order)
        #print(tm_checklist_id, type(tm_checklist_id))
        if bm_checklist_id is not None:
            return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': bm_checklist_id}))
        else:
            return HttpResponse('Ошибка при создании чек листа')