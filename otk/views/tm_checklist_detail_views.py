from django.views.generic import DetailView

from otk.models.order import OTKOrder
from otk.models.order import TMCheckList
from otk.models.order import RM6CheckList

from django.urls import reverse

from otk.utils import model_to_dict_verbose


    
class TMCheckListDetailView(DetailView):
    model = TMCheckList
    template_name = "tm_checklist_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(TMCheckListDetailView, self).get_context_data(**kwargs)

        context['man_number'] = self.object.otkorder.man_number
        
        context['chlist_dict'] = model_to_dict_verbose(self.object, exclude=['id'])
        
        sktm = self.object.sktmchecklist_set.all()
        context['sktm'] = model_to_dict_verbose(sktm[0], exclude=['id', 'checklist'])

        srtm = self.object.srtmchecklist_set.all()
        context['srtm'] = {}
        if len(srtm) > 0:
            context['srtm'] = model_to_dict_verbose(srtm[0], exclude=['id', 'checklist'])

        ktmue = self.object.ktmuechecklist_set.all()
        context['ktmue'] = {}
        if len(ktmue) > 0:
            context['ktmue'] = model_to_dict_verbose(ktmue[0], exclude=['id', 'checklist'])

        context['rm6s'] = {}
        rm6s = self.object.rm6checklist_set.all()
        if len(rm6s) > 0:
            for i in range(len(rm6s)):
                rm = {}
                rm["rm6-"] = ' '
                rm.update(model_to_dict_verbose(rm6s[i], exclude=['id', 'checklist']))
                rm = {str(key) + '(' + str(i+1) + ')' : val for key, val in rm.items()}
                context['rm6s'].update(rm)

        context['ybp'] = {}
        ybp = self.object.ybpchecklist_set.all()
        if len(ybp) > 0:
            for i in range(len(ybp)):
                y = {}
                y["ybp-"] = ' '
                y.update(model_to_dict_verbose(ybp[i], exclude=['id', 'checklist']))
                y = {str(key) + '(' + str(i+1) + ')' : val for key, val in y.items()}
                context['ybp'].update(y)

        context['su'] = {}
        su = self.object.suchecklist_set.all()
        if len(su) > 0:
            for i in range(len(su)):
                y = {}
                y["su-"] = ' '
                y.update(model_to_dict_verbose(su[i], exclude=['id', 'checklist']))
                y = {str(key) + '(' + str(i+1) + ')' : val for key, val in y.items()}
                context['su'].update(y)
        # print(model_to_dict_verbose(rm6s[0], exclude=['id']), len(rm6s))
        # context['rm6s'] = self.object.rm6checklist_set.all()

        return context