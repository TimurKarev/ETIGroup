from django.views.generic import TemplateView

from otk.models.checklists import ChListSection


# TODO дописать для всего
from otk.services.order_services import get_section_context


def get_order_number_by_section(section_entry):
    try:
        return section_entry.checklist.bm_checklist.man_number
    except:
        return None


class CheckListConfigUpdateView(TemplateView):
    template_name = 'checklist_config_update.html'

    def get_context_data(self, **kwargs):

        config_section = ChListSection.objects.get(id=kwargs['pk'])

        context = {'order_number': get_order_number_by_section(config_section)}

        request = None
        if self.request.POST:
            return self.request.POST

        full_data = get_section_context(config_section, request)
        context['config'] = full_data['points']

        print(context)