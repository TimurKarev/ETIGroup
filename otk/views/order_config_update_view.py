from otk.services.order_services import get_section_context, get_config_section_from_order_id
from otk.views.mixins.user_access_mixin import UserAccessMixin

from django.http import HttpResponseRedirect
from django.urls import reverse

from otk.models.otk_order import OTKOrder

from django.views.generic import TemplateView


class OrderConfigUpdateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_config_update.html'

    class_type = 'order_config_update_view'

    def get_context_data(self, **kwargs):
        #context = super(OrderConfigUpdateView, self).get_context_data(**kwargs)
        context = {}
        if self.request.POST:
            post = self.request.POST
        else:
            post = None

        context['order_number'] = OTKOrder.objects.get(id=kwargs['pk'])
        context['section'] = get_section_context(
            get_config_section_from_order_id(int(kwargs['pk'])),
            post
        )
        # print(context)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # print('OrderConfigUpdateView', context['section'])

        # TODO сделать нормальную валидацию
        for point in context['section']['points']:
            point['form'].is_valid()
            # print(point['form'].cleaned_data)
            point['form'].save()

        return HttpResponseRedirect(
            reverse('order_detail', kwargs={'pk': kwargs['pk']})
        )

