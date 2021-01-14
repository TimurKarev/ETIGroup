import json

from django.http import HttpResponseRedirect
from django.urls import reverse

from otk.services.services import get_order_by_checklist, get_detail_context_from_checklist_object
from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.models.checklists import *


class CheckListDetailView(UserAccessMixin, TemplateView):
    permission_required = 'otk.view_checklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = "checklist_detail.html"

    def get_context_data(self, **kwargs):
        #'checklist': self._checklist_entry, 'checklist_type': kwargs['tp']
        context = {}

        data = get_detail_context_from_checklist_object(self._checklist_entry, form=False)

        self._is_data_empty = not data

        context['data'] = data
        context['checklist_name'] = self._checklist_entry.name
        context['pk'] = self._checklist_entry.id
        context['checklist_type'] = kwargs['tp']

        return {"j_checklist_detail": json.dumps(context)}

    def get(self, request, *args, **kwargs):
        self._checklist_entry = Checklist.objects.get(id=kwargs['pk'])
        self.get_context_data(**kwargs)

        if self._is_data_empty:
            try:
                order_id = get_order_by_checklist(self._checklist_entry, kwargs['tp']).id
                return HttpResponseRedirect(reverse
                                            ('checklist_sections_create',
                                             kwargs={'pk': order_id, 'tp': kwargs['tp']})
                                            )
            except Exception as e:
                print(e)

        return super(CheckListDetailView, self).get(request, *args, **kwargs)
