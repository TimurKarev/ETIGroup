from django.urls import path
from otk.views.views import CheckListListView

urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),
    #path('/?print_btn=Click', CheckListListView.as_view(), name='checklist_list'),
]
