# from otk.views.mixins.user_access_mixin import UserAccessMixin
#
# from otk.services.services import create_tmchecklist_from_order_model
#
# from django.views.generic import TemplateView
#
#
# from otk.models.otk_order import OTKOrder
# from otk.models.tm_checklists import *
#
# from django.urls import reverse
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
#
#
# class TMCheckListCreateView(UserAccessMixin, TemplateView):
#     permission_required = 'otk.add_otkchecklist'
#     raise_exception = False
#     redirect_without_permission = 'checklist_list'
#
#     template_name = 'tm_checklist_create.html'
#
#
#     def get(self, request, *args, **kwargs):
#         tm_checklist_id = create_tmchecklist_from_order_model(int(kwargs['pk']))
#         print(tm_checklist_id, type(tm_checklist_id))
#         if tm_checklist_id is not None:
#             return HttpResponseRedirect(reverse('tm_checklist_update', kwargs={'pk': tm_checklist_id}))
#         else:
#             return HttpResponse('Ошибка при создании чек листа')
        