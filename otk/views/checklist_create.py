from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import RedirectView

from otk.models.otk_order import OTKOrder

from otk.services.services import get_checklist_name_by_type, get_checklist_for_order_by_type, get_config_data_by_type, \
    create_config_section_by_data
from otk.views.mixins.user_access_mixin import UserAccessMixin


class CheckListCreateView(UserAccessMixin, RedirectView):
    permission_required = 'otk.add_checklist'
    raise_exception = False
    redirect_without_permission = 'chlist'

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
