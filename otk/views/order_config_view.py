from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import TemplateView

from otk.services.services import get_json_file

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from otk.models.otk_order import OTKOrder

import json


class OrderConfigCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'order_config_create.html'

    order_checklist_type = 'order_config'

    def get(self, request, *args, **kwargs):
        order_entry = OTKOrder.objects.get(id=int(kwargs['pk']))
        config_section_entry = order_entry.config_section

        print('OrderConfigCreateView', kwargs)
        self.create_config(config_section_entry)
        # checklist_id = create_checklist_from_json(
        #     order,
        #     self.el_checklist_type,
        #     checklist_name
        # )

        # if checklist_id is not None:
        #     return HttpResponseRedirect(reverse('checklist_detail', kwargs={'pk': checklist_id}))
        # else:
        return HttpResponse('Мы на нужной странице')

    def create_config(self, config_section_entry):
        json_path = get_json_file(self.order_checklist_type)
        print(json_path)

        with open(
                json_path,
                "r", encoding="utf-8"
        ) as read_file:
            sections = json.load(read_file)
            print(sections)

            for point in sections[0]['points']:
                print(point['name'])
