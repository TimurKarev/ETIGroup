from otk.views.mixins.user_access_mixin import UserAccessMixin
from django.views.generic import DetailView

from otk.models.checklists import Checklist

class CheckListDetailView(UserAccessMixin, DetailView):
    permission_required = 'otk.view_otkchecklist'
    raise_exception = False
    redirect_without_permission = 'checklist_list'
    
    model = Checklist
    template_name = "checklist_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(CheckListDetailView, self).get_context_data(**kwargs)