from django.urls import path
from otk.views.views import CheckListListView
from otk.views.tm_checklist_views import (TMCheckListCreateView,
                                        TMCheckListUpdateView)

urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),
    path('tm_checklist_create/<int:pk>/', TMCheckListCreateView.as_view(), name='tm_checklist_create'),
    #path('tm_checklist_detail/<int:pk>/', TMCheckListDetailView.as_view(), name='tm_checklist_detail'),
    path('tm_checklist_update/<int:pk>/', TMCheckListUpdateView.as_view(), name='tm_checklist_update'),
]
