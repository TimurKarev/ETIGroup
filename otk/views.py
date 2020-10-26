from django.views.generic import ListView, DetailView

from .models import TMCheckList

# Create your views here.
class CheckListListView(ListView):
    model = TMCheckList
    template_name = 'checklist_list.html'
    
class CkeckListDetailView(DetailView):
    model = TMCheckList
    template_name = 'checklist_detail.html'