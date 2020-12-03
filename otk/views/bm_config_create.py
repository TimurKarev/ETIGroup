from django.views.generic import RedirectView

from otk.models.otk_order import OTKOrder
from otk.services.services import create_checklist, create_cl_section_entry, get_json_data, create_point_entry
from otk.views.bm_checklist_create import BMCheckListCreateView
from otk.views.mixins.user_access_mixin import UserAccessMixin


class BMConfigCreateView(UserAccessMixin, RedirectView):
    permission_required = 'otk.add_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    bm_config_type = 'bm_config'

    pattern_name = 'bm_config_update'

    def get_redirect_url(self, *args, **kwargs):
        check_list_id = self.get_checklist_with_config(int(kwargs['pk']))
        return super().get_redirect_url(kwargs={'pk': check_list_id})

    def get_checklist_with_config(self, order_id):
        order_entry = OTKOrder.objects.get(id=order_id)
        checklist_name = "Чеклист строительной части, заказ №" + str(order_entry.man_number)
        check_list = create_checklist(checklist_name)

        section_entry = create_cl_section_entry('config', check_list)
        config_points = get_json_data(BMCheckListCreateView.bm_checklist_type, config=True)
        print(config_points)
        for i, point in enumerate(config_points):
            create_point_entry(point, i + 1, section_entry)

        order_entry.bm_checklist = check_list
        order_entry.save()
        return check_list.id
