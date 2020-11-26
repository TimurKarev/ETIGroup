from otk.services.order_services import get_section_context, get_config_section_from_order_id
from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.http import HttpResponse, HttpResponseRedirect

from otk.models.otk_order import OTKOrder

from django.views.generic import TemplateView


class OrderConfigUpdateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_config_update.html'

    class_type = 'order_config_update_view'

    def get_context_data(self, **kwargs):
        context = super(OrderConfigUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data = self.request.POST
        else:
            data = None

        print('DATA  - ', data)

        context['section'] = get_section_context(
            get_config_section_from_order_id(int(kwargs['pk'])),
            data
        )

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print(context['section'])
        for point in context['section']:
            point['form'].is_valid()
            print(point['form'].cleaned_data)
            point['form'].save()

