from otk.views.mixins.user_access_mixin import UserAccessMixin

from otk.models.order import OTKOrder

from django.views.generic import  FormView

from otk.views.forms.model_forms import SubstationTypePointForm

class OrderCreateView(UserAccessMixin, FormView):
    permission_required = 'otk.add_order'
    redirect_without_permission = 'checklist_list'
    
    #model = OTKOrder
    form_class = SubstationTypePointForm
    template_name = 'order_create.html'
    fields = ['man_number']

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['type'] = SubstationTypePointForm
        
        if self.request.POST:
            print ('POST')
            context['type'] = SubstationTypePointForm(data = self.request.POST)

        print("context   ", context['type'])
        
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        print(type(form))
        print(context['type'].cleaned_data)
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"
        #return super(ContactView, self).form_valid(form)
        