from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView

from otk.models.checklists import Checklist

from django.forms.models import inlineformset_factory

from otk.models.checklists import *

from otk.services.context_creators import *

from django import forms


class CheckListUpdateView(TemplateView):
    template_name = 'checklist_update.html'

    def get_context_data(self, **kwargs):
        # context = super(CheckListUpdateView, self).get_context_data(**kwargs)

        checklist_entry = Checklist.objects.get(id=kwargs['pk'])
        context = {'checklist_name': checklist_entry.name}

        if self.request.POST:
            post = self.request.POST
        else:
            post = None

        context['sections'] = get_detail_context_from_checklist_object(
            checklist_entry, post
        )

        for section in context['sections']:
            for i, point in enumerate(section['points']):
                if (point['value'] == 'НЕ Принято') or (point['value'] == 'Принято'):
                    section['points'].pop(i)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # TODO сделать нормальную валидацию
        for section in context['sections']:
            for point in section['points']:
                point['form'].is_valid()
                point['form'].save()

        # update_yesno_fields()
        #        return "/checklist_detail/" + str(self.object.id)
        return HttpResponseRedirect(
            reverse('checklist_detail',
                    kwargs={'pk': kwargs['pk']})
        )
