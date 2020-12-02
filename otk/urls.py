from django.urls import path

from otk.views.bm_config_create import BMConfigCreateView
from otk.views.bm_config_update_view import BMConfigUpdateView
from otk.views.checklist_config_update import CheckListConfigUpdateView
from otk.views.checklist_create import CheckListCreateView
from otk.views.checklist_sections_create import CheckListSectionsCreateView
from otk.views.order_config_create_view import OrderConfigCreateView
from otk.views.order_config_update_view import OrderConfigUpdateView
from otk.views.views import CheckListListView
from otk.views.order_create_view import OrderCreateView
from otk.views.tm_checklist_create_view import TMCheckListCreateView
from otk.views.tm_checklist_update_view import TMCheckListUpdateView
from otk.views.tm_checklist_detail_views import TMCheckListDetailView
from otk.views.checklist_detail_view import CheckListDetailView
from otk.views.checklist_update_view import CheckListUpdateView
from otk.views.bm_checklist_create import BMCheckListCreateView
from otk.views.el_checklist_create import ELCheckListCreateView
from otk.views.order_detail_view import OrderDetailView


urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),

    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_create_config/<int:pk>/', OrderConfigCreateView.as_view(), name='order_create_config'),
    path('order_update_config/<int:pk>/', OrderConfigUpdateView.as_view(), name='order_update_config'),
    path('order_detail_view/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    path('bm_config_create/<int:pk>', BMConfigCreateView.as_view(), name='bm_config_create'),
    path('bm_config_update/<int:pk>', BMConfigUpdateView.as_view(), name='bm_config_update'),

    path('checklist_create/<slug:tp>/<int:pk>', CheckListCreateView.as_view(), name='checklist_create'),
    path('checklist_config_update/<slug:tp>/<int:pk>', CheckListConfigUpdateView.as_view(), name='checklist_config_update'),
    path('checklist_sections_create/<slug:tp>/<int:pk>', CheckListSectionsCreateView.as_view(), name='checklist_sections_create'),


    path('tm_checklist_create/<int:pk>/', TMCheckListCreateView.as_view(), name='tm_checklist_create'),
    path('tm_checklist_detail/<int:pk>/', TMCheckListDetailView.as_view(), name='tm_checklist_detail'),
    path('tm_checklist_update/<int:pk>/', TMCheckListUpdateView.as_view(), name='tm_checklist_update'),
    path('bm_checklist_create/<int:pk>/', BMCheckListCreateView.as_view(), name='bm_checklist_create'),
    path('el_checklist_create/<int:pk>/', ELCheckListCreateView.as_view(), name='el_checklist_create'),
    path('checklist_detail/<int:pk>/', CheckListDetailView.as_view(), name='checklist_detail'),
    path('checklist_update/<int:pk>/', CheckListUpdateView.as_view(), name='checklist_update'),
]
