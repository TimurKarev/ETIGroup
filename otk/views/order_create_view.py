from django.urls import reverse

from otk.services.order_services import create_order
from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView

from otk.views.forms.model_forms import SubstationTypePointForm, OTKOrderForm


class OrderCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_create.html'

    class_type = 'order_create_view'

# TODO сделать сохранение введенных параметров после перезагрузки
    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)

        # print(self.request.POST)
        # TODO проверить на уникальность номер
        context['order'] = OTKOrderForm(data=(self.request.POST or None))
        context['type'] = SubstationTypePointForm(data=(self.request.POST or None))

        # print(context)

        return context

    def post(self, request, *args, **kwargs):
        order = OTKOrderForm(data=request.POST)
        type_form = SubstationTypePointForm(data=request.POST)
        if order.is_valid() and type_form.is_valid():
            # print(order.cleaned_data, type_form.cleaned_data)
            order_num = order.cleaned_data['man_number']
            type_string = type_form.cleaned_data['point_value']
            order_id = create_order(order_num, type_string)
            if order_id is False:
                return HttpResponse(str.format(f'Не удалось создать зааз'))
        else:
            return HttpResponse(str.format(
                f'Ошибка валидации \n {order.errors} \n {type_form.errors}'))

        return HttpResponseRedirect(reverse('order_create_config', kwargs={'pk': order_id}))

