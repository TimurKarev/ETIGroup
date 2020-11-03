from django.forms.models import inlineformset_factory

from django.views.generic.edit import  UpdateView

from otk.models.order import OTKOrder
from otk.models.tm_checklists import *
# from otk.models.order import RM6CheckList
# from otk.models.order import SKTMCheckList

#TODO убрать ACCEPTED fields from 

RM6Formset = inlineformset_factory(
    TMCheckList, RM6CheckList, exclude=('id',), extra = 0,
)
SKTMFormset = inlineformset_factory(
    TMCheckList, SKTMCheckList, exclude=('id',), extra = 0,
)
SRTMFormset = inlineformset_factory(
    TMCheckList, SRTMCheckList, exclude=('id',), extra = 0,
)
KTMUEFormset = inlineformset_factory(
    TMCheckList, KTMUECheckList, exclude=('id',), extra = 0,
)
YBPFormset = inlineformset_factory(
    TMCheckList, YBPCheckList, exclude=('id',), extra = 0,
)
SUFormset = inlineformset_factory(
    TMCheckList, SUCheckList, exclude=('id',), extra = 0,
)

class TMCheckListUpdateView(UpdateView):
    model = TMCheckList
    #form_class = UpdateTMChecklistForm
    template_name = "tm_checklist_update.html"
    fields = '__all__'
    success_url = '/tm_checklist_detail/'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["rm6"] = RM6Formset(self.request.POST, instance=self.object)
            data["sktm"] = SKTMFormset(self.request.POST, instance=self.object)
            data["srtm"] = SRTMFormset(self.request.POST, instance=self.object)
            data["ktmue"] = KTMUEFormset(self.request.POST, instance=self.object)
            data["ybp"] = YBPFormset(self.request.POST, instance=self.object)
            data["su"] = SUFormset(self.request.POST, instance=self.object)
        else:
            data["rm6"] = RM6Formset(instance=self.object)
            data["sktm"] = SKTMFormset(instance=self.object)
            data["srtm"] = SRTMFormset(instance=self.object)
            data["ktmue"] = KTMUEFormset(instance=self.object)
            data["ybp"] = YBPFormset(instance=self.object)
            data["su"] = SUFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        su = context["su"]
        if su.is_valid():
            su.instance = self.object
            su.save()

        rm6 = context["rm6"]
        if rm6.is_valid():
            rm6.instance = self.object
            rm6.save()

        ybp = context["ybp"]
        if ybp.is_valid():
            ybp.instance = self.object
            ybp.save()

        sktm = context["sktm"]
        if sktm.is_valid():
            sktm.instance = self.object
            sktm.save()

        srtm = context["srtm"]
        if srtm.is_valid():
            srtm.instance = self.object
            srtm.save()

        ktmue = context["ktmue"]
        if ktmue.is_valid():
            ktmue.instance = self.object
            ktmue.save()

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return "/tm_checklist_detail/" + str(self.object.id)