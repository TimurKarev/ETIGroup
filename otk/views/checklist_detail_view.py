from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import DetailView

from otk.models.checklists import *

from otk.services.context_creators import get_detail_context_from_checklist_object


class CheckListDetailView(UserAccessMixin, DetailView):
    permission_required = 'otk.view_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'

    model = Checklist
    template_name = "checklist_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CheckListDetailView, self).get_context_data(**kwargs)

        data = get_detail_context_from_checklist_object(self.object)

        context['data'] = data
        print(data)

        return context
