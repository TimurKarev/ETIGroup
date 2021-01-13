import json

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView

from otk.models.checklists import Checklist
from otk.services.services import get_detail_context_from_checklist_object, update_yesno_fields


class CheckListUpdateView(TemplateView):
    template_name = 'checklist_update.html'

    def get_context_data(self, **kwargs):
        # context = super(CheckListUpdateView, self).get_context_data(**kwargs)

        checklist_entry = Checklist.objects.get(id=kwargs['pk'])
        self._checklist_entry = checklist_entry
        context = {'checklist_name': checklist_entry.name, 'pk': kwargs['pk'], 'type': kwargs['tp']}

        if self.request.POST:
            post = self.request.POST
        else:
            post = None

        context['sections'] = get_detail_context_from_checklist_object(checklist_entry)

        for section in context['sections']:
            for i, point in enumerate(section['points']):
                if (point['value'] == 'Пройдены') or (point['value'] == 'Не Пройдены'):
                    section['points'].pop(i)

        #print("checklist_update", context)
        return {"j_checklist_update_data": json.dumps(context)}

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # TODO сделать нормальную валидацию
        for section in context['sections']:
            for point in section['points']:
                point['form'].is_valid()
                point['form'].save()

        update_yesno_fields(self._checklist_entry)
        #        return "/checklist_detail/" + str(self.order_entry.id)
        return HttpResponseRedirect(
            reverse('checklist_detail',
                    kwargs={'tp': kwargs['tp'], 'pk': kwargs['pk']})
        )

