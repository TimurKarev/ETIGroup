import json

from django.http import JsonResponse
from django.urls import reverse

from django.views.generic import TemplateView

from otk.models.checklists import ChListSection, IntegerPoint

# TODO дописать для всего
from otk.services.services import get_order_by_checklist, get_section_context, update_point_values_by_point_list
from otk.views.mixins.user_access_mixin import UserAccessMixin


class CheckListConfigUpdateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_checklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    template_name = 'checklist_config_update.html'

    def get_context_data(self, **kwargs):
        config_section = ChListSection.objects.get(id=kwargs['pk'])
        self.order = get_order_by_checklist(config_section.checklist, kwargs['tp'])
        order_man_number = self.order.man_number
        context = {'order_number': order_man_number}

        request = None
        if self.request.POST:
            request = self.request.POST

        full_data = get_section_context(config_section, request)
        context['config'] = full_data['points']
        context['pk'] = kwargs['pk']

        return {"j_checklist_config_update_data": json.dumps(context)}

    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body)
        print(CheckListConfigUpdateView.__name__, post_data, type(post_data))

        update_point_values_by_point_list(post_data['points'])

        config_section = ChListSection.objects.get(id=kwargs['pk'])
        self.order = get_order_by_checklist(config_section.checklist, kwargs['tp'])

        response = reverse('checklist_sections_create',
                           kwargs={'tp': kwargs['tp'], 'pk': self.order.id})

        return JsonResponse({"message": response})
