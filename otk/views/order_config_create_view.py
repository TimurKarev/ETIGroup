from otk.services.order_services import get_config_section_from_order_id
from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic.base import RedirectView

from otk.services.services import get_json_file, create_integer_point_entry, create_string_point_entry

from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from otk.models.otk_order import OTKOrder

import json


class OrderConfigCreateView(UserAccessMixin, RedirectView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

# TODO делать рефактор названий классов, url pattern & класс строчек
    order_checklist_type = 'order_config'

    pattern_name = 'order_update_config'

    def get_redirect_url(self, *args, **kwargs):

        config_section_entry = get_config_section_from_order_id(int(kwargs['pk']))
        self.create_config(config_section_entry)

        print(args, kwargs)
        return super().get_redirect_url(*args, **kwargs)

    def create_config(self, config_section_entry):
        json_path = get_json_file(self.order_checklist_type)
        print(json_path)

        with open(
                json_path,
                "r", encoding="utf-8"
        ) as read_file:
            sections = json.load(read_file)

        config_section = None
        for section in sections:
            if section['name'] == 'config':
                try:
                    config_section = section['points']
                except Exception as e:
                    print(e)
                    return None
                break

        if config_section is None:
            return None
        # TODO add more points in creation
        for i, point in enumerate(config_section):
            if point['point_type'] == 'integer':
                create_integer_point_entry(
                    point['name'],
                    point['value'],
                    i + 1,
                    config_section_entry,
                    True)
            elif point['point_type'] == 'string':
                create_string_point_entry(
                    point['name'],
                    point['value'],
                    i + 1,
                    config_section_entry,
                    True)

