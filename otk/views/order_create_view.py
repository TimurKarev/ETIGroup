from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.otk_order import OTKOrder

from django.views.generic import FormView

from otk.views.forms.model_forms import SubstationTypePointForm, OTKOrderForm


class OrderCreateView(UserAccessMixin, FormView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'

    model = OTKOrder
    form_class = OTKOrderForm
    template_name = 'order_create.html'
    fields = ['man_number']

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['type'] = SubstationTypePointForm(data=self.request.POST)
        else:
            context['type'] = SubstationTypePointForm()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        print(form.cleaned_data)
        c = context['type']
        if c.is_valid():
            print(c.cleaned_data)
        else:
            print('huj')
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        # print "form is valid"
        # return super(ContactView, self).form_valid(form)

    # def form_invalid(self, form):
    #     context = self.get_context_data()
    #     print('Error', form.errors)
