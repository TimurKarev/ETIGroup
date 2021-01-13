from otk.services.order_services import get_config_section_from_order_id
from otk.services.services import get_section_context, update_point_values_by_dict_list
from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.http import JsonResponse

from otk.models.otk_order import OTKOrder

from django.views.generic import TemplateView
import json


class OrderConfigUpdateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_config_update.html'

    class_type = 'order_config_update_view'

    def get_context_data(self, **kwargs):

        if self.request.POST:
            post = self.request.POST
        else:
            post = None

        man_number = OTKOrder.objects.get(id=kwargs['pk']).man_number
        pk = kwargs['pk']
        section = get_section_context(
            get_config_section_from_order_id(int(kwargs['pk'])),
            post
        )

        config = {
            "pk": pk,
            "man_number": man_number,
            "points": section['points']
        }
        json_data = json.dumps(config)

        return {'j_order_config_data': json_data}

    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body)
        # print(OrderConfigUpdateView.__name__, post_data, type(post_data))
        response = update_point_values_by_dict_list(post_data['points'])

        return JsonResponse({"message": response})
