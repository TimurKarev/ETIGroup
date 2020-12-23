from otk.services.order_services import get_config_section_from_order_id
from otk.services.services import get_section_context
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
            #del post['csrfmiddlewaretoken']
        else:
            post = None

        context['order_number'] = OTKOrder.objects.get(id=kwargs['pk'])
        context['section'] = get_section_context(
            get_config_section_from_order_id(int(kwargs['pk'])),
            post
        )
        #print(context['section']['points'][0]['form'])
        return context

    def post(self, request, *args, **kwargs):
        print(OrderConfigUpdateView.__name__, request.POST)
        context = self.get_context_data(**kwargs)
        #print('OrderConfigUpdateView', context['section']['points'][0]['form'])
        #f = context['section']['points'][0]['form']

        # TODO сделать нормальную валидацию
        for point in context['section']['points']:
            point['form'].is_valid()
            #print(point['form'].cleaned_data)
            point['form'].save()
        print(OrderConfigUpdateView.__name__, 'GOGOG')

        return HttpResponseRedirect(
            reverse('order_detail', kwargs={'pk': kwargs['pk']})
        )

