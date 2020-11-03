from django.urls import path
from otk.views.views import CheckListListView, OrderCreateView
from otk.views.tm_checklist_create_view import TMCheckListCreateView
from otk.views.tm_checklist_update_view import TMCheckListUpdateView
from otk.views.tm_checklist_detail_views import TMCheckListDetailView 

urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('tm_checklist_create/<int:pk>/', TMCheckListCreateView.as_view(), name='tm_checklist_create'),
    path('tm_checklist_detail/<int:pk>/', TMCheckListDetailView.as_view(), name='tm_checklist_detail'),
    path('tm_checklist_update/<int:pk>/', TMCheckListUpdateView.as_view(), name='tm_checklist_update'),
]
