import json

from django.urls import reverse
from django.db import models

from otk.models.otk_order import OTKOrder
from otk.services.order_services import create_order
from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views.generic import TemplateView

from otk.views.forms.model_forms import SubstationTypePointForm, OTKOrderForm


class OrderCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_otkorder'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_create.html'

    class_type = 'order_create_view'

# TODO сделать сохранение введенных параметров после перезагрузки
    def get_context_data(self, **kwargs):
        # context = super(OrderCreateView, self).get_context_data(**kwargs)
        man_number_list = [num.man_number for num in OTKOrder.objects.all()]
        redirect_link = reverse('order_create_config', kwargs={'pk': 0})
        tp_type_list = ['БКТП']

        context = {
            "man_number_list": man_number_list,
            "redirect_link": redirect_link,
            "tp_type_list": tp_type_list,
        }

        return {"j_order_create_data": json.dumps(context)}

    def post(self, request, *args, **kwargs):
        # order = OTKOrderForm(data=request.POST)
        # type_form = SubstationTypePointForm(data=request.POST)
        # if order.is_valid() and type_form.is_valid():
        #     # print(order.cleaned_data, type_form.cleaned_data)
        #     order_num = order.cleaned_data['man_number']
        #     type_string = type_form.cleaned_data['point_value']
        #     order_id = create_order(order_num, type_string)
        #     if order_id is False:
        #         return HttpResponse(str.format(f'Не удалось создать зааз'))
        # else:
        #     return HttpResponse(str.format(
        #         f'Ошибка валидации \n {order.errors} \n {type_form.errors}'))
        #
        # return HttpResponseRedirect(reverse('order_create_config', kwargs={'pk': order_id}))
        post_data = json.loads(request.body)
        #print("ordeer_create", post_data)
        order_id = create_order(post_data['order_num'], post_data['order_type'])
        response_data = {'status': 'error'}
        if order_id:
            response_data['status'] = 'ok'
            response_data['id'] = order_id
        return JsonResponse(response_data)
