from django.views.generic import UpdateView

from django.forms.models import inlineformset_factory

from otk.models.checklists import *

from otk.services.context_creators import *


from django import forms

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = []
        


class CheckListUpdateView(UpdateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'checklist_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['sections'] = get_update_context_from_checklist_object(self.object, self.request.POST)
        else:
            context['sections'] = get_update_context_from_checklist_object(self.object)
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()

        save_all_formsets(context, self.object)
        
        return super().form_valid(form)


    def get_success_url(self):
        return "/checklist_detail/" + str(self.object.id)
