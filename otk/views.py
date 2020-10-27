from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import TMCheckList

# Create your views here.
class CheckListListView(ListView):
    model = TMCheckList
    template_name = 'checklist_list.html'
    
class CkeckListDetailView(DetailView):
    model = TMCheckList
    template_name = 'checklist_detail.html'
    
class CheckListListCreate(CreateView):
    model = TMCheckList
    template_name = 'checklist_new.html'
    fields = '__all__'

class CheckListListEdit(UpdateView):
    model = TMCheckList
    template_name = 'checklist_edit.html'
    fields = '__all__'