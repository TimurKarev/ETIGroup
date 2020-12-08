from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView

from otk.models.checklists import ChListSection

# TODO дописать для всего
from otk.services.services import get_order_by_checklist, get_section_context


class CheckListConfigUpdateView(TemplateView):
    template_name = 'checklist_config_update.html'

    def get_context_data(self, **kwargs):
        config_section = ChListSection.objects.get(id=kwargs['pk'])
        self.order = get_order_by_checklist(config_section.checklist, kwargs['tp'])
        order_man_number = self.order.man_number
        context = {'order_number': order_man_number}

        request = None
        if self.request.POST:
            request = self.request.POST

        full_data = get_section_context(config_section, request)
        context['config'] = full_data['points']

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # print(context)
        # TODO сделать нормальную валидацию
        for form in context['config']:
            form['form'].is_valid()
            # print(form['form'].cleaned_data)
            form['form'].save()

        return HttpResponseRedirect(
            reverse('checklist_sections_create',
                    kwargs={'tp': kwargs['tp'], 'pk': self.order.id})
        )

