from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.otk_order import OTKOrder

from django.views.generic import TemplateView

from otk.views.forms.model_forms import SubstationTypePointForm, OTKOrderForm


class OrderCreateView(UserAccessMixin, TemplateView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    template_name = 'order_create.html'

    class_type = 'order_create_view'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)

        print(self.request.POST)
        # TODO проверить на уникальность номер
        context['order'] = OTKOrderForm(data=(self.request.POST or None))
        context['type'] = SubstationTypePointForm(data=(self.request.POST or None))

        print(context)

        return context

    def post(self, request, *args, **kwargs):
        order = OTKOrderForm(data=request.POST)
        type = SubstationTypePointForm(data=request.POST)
        if order.is_valid() and type.is_valid():
            print(order.cleaned_data, type.cleaned_data)


