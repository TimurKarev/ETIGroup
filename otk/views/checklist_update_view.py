from django.views.generic import UpdateView

from django.forms.models import inlineformset_factory

from otk.models.checklists import *

from otk.services.context_creators import *


from django import forms

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = []
        

class FourChoisePointForm(forms.ModelForm):
    class Meta:
        model = FourChoisePoint
        fields = ['choise', 'comment']


FourChoisePointFormset = inlineformset_factory(
    ChListSection, FourChoisePoint, exclude=('id', 'name'), extra = 0,
)

class CheckListUpdateView(UpdateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'checklist_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        section = self.object.chlistsection_set.all()[0]
        if self.request.POST:
            context['four'] = FourChoisePointFormset(self.request.POST, instance=section)
        else:
            context['four'] = FourChoisePointFormset(instance=section)
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()

        su = context["four"]
        if su.is_valid():
            su.instance = self.object.chlistsection_set.all()[0]
            su.save()

        return super().form_valid(form)

    # def form_invalid(self, form):
    #     context = self.get_context_data()
    #     print('INVALID', context)
    #     return super().form_invalid(form)

    def get_success_url(self):
        return "/checklist_detail/" + str(self.object.id)
        

    # def get(self, request, *args, **kwargs):
    #     # The Publisher we're editing:
    #     self.object = self.get_object(queryset=Publisher.objects.all())
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     # The Publisher we're uploading for:
    #     self.object = self.get_object(queryset=Publisher.objects.all())
    #     return super().post(request, *args, **kwargs)

    # def get_form(self, form_class=None):
    #     """
    #     Use our big formset of formsets, and pass in the Publisher object.
    #     """
    #     return PublisherBooksWithImagesFormset(
    #                         **self.get_form_kwargs(), instance=self.object)

    # def form_valid(self, form):
    #     """
    #     If the form is valid, redirect to the supplied URL.
    #     """
    #     form.save()

    #     messages.add_message(
    #         self.request,
    #         messages.SUCCESS,
    #         'Changes were saved.'
    #     )

    #     return HttpResponseRedirect(self.get_success_url())

    # def get_success_url(self):
    #     return reverse('books:publisher_detail', kwargs={'pk': self.object.pk})