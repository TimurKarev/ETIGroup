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
        self._checklist_entry = checklist_entry
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
                if (point['value'] == 'Пройдены') or (point['value'] == 'Не Пройдены'):
                    section['points'].pop(i)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # TODO сделать нормальную валидацию
        for section in context['sections']:
            for point in section['points']:
                point['form'].is_valid()
                point['form'].save()

        update_yesno_fields(self._checklist_entry)
        #        return "/checklist_detail/" + str(self.object.id)
        return HttpResponseRedirect(
            reverse('checklist_detail',
                    kwargs={'pk': kwargs['pk']})
        )


def update_yesno_fields(checklist_entry: Checklist):
    sections = checklist_entry.chlistsection_set.all()
    for section in sections:
        yesno_points = section.yesnochoicepoint_set.all()
        if len(yesno_points) > 0:
            yesno_point = yesno_points[0]
            # print(yesno_point, "  ---- ",  section.name)
            four_points = section.fourchoicepoint_set.all()
            is_no_value = False
            for four_point in four_points:
                if four_point.point_value == four_point.Four.UNCHECKED or \
                        four_point.point_value == four_point.Four.COMMENT:
                    is_no_value = True
                    try:
                        yesno_point.point_value = yesno_point.YesNo.NO
                        yesno_point.save()
                        break
                    except Exception as e:
                        print(e)

            if not is_no_value:
                try:
                    yesno_point.point_value = yesno_point.YesNo.YES
                    yesno_point.save()
                except Exception as e:
                    print(e)
