from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views.generic import RedirectView

from otk.models.otk_order import OTKOrder

from otk.services.services import get_json_data, create_cl_section_entry, \
    create_point_entry, get_checklist_name_by_type, get_checklist_for_order_by_type


def get_config_data_by_type(tp):
    config_data = get_json_data(tp, True)
    return config_data


def create_config_section_by_data(checklist, config_data):
    existing_sections = checklist.chlistsection_set.all()
    config_section = None
    if len(existing_sections) > 0:
        config_section = existing_sections.filter(name='config')[0]

    if config_section is not None:
        return config_section.id

    config_section = create_cl_section_entry('config', checklist)
    if config_section is None:
        return None

    for i, point in enumerate(config_data['points']):
        create_point_entry(point, i + 1, config_section)

    return config_section.id


class CheckListCreateView(RedirectView):

    def get(self, request, *args, **kwargs):
        super(CheckListCreateView, self).get(request, *args, **kwargs)

        order = OTKOrder.objects.get(id=int(kwargs['pk']))

        checklist_name = get_checklist_name_by_type(kwargs['tp'], order.man_number)

        checklist = get_checklist_for_order_by_type(order, kwargs['tp'], checklist_name)

        config_data = get_config_data_by_type(kwargs['tp'])

        # TODO coздаем универсальнуй функцию для создания полного чеклиста
        if config_data is None:
            return HttpResponseRedirect(
                reverse('checklist_sections_create',
                        kwargs={'tp': kwargs['tp'], 'pk': int(order.id)}))

        section_id = create_config_section_by_data(checklist, config_data)

        return HttpResponseRedirect(
            reverse('checklist_config_update',
                    kwargs={'tp': kwargs['tp'], 'pk': int(section_id)}))
