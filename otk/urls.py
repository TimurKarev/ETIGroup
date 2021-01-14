from django.urls import path

from otk.views.checklist_config_update import CheckListConfigUpdateView
from otk.views.checklist_create import CheckListCreateView
from otk.views.checklist_sections_create import CheckListSectionsCreateView
from otk.views.login_view import LoginView
from otk.views.order_config_create_view import OrderConfigCreateView
from otk.views.order_config_update_view import OrderConfigUpdateView
from otk.views.check_list_list_view import CheckListListView
from otk.views.order_create_view import OrderCreateView
from otk.views.checklist_detail_view import CheckListDetailView
from otk.views.checklist_update_view import CheckListUpdateView
from otk.views.order_detail_view import OrderDetailView


urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),

    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_create_config/<int:pk>/', OrderConfigCreateView.as_view(), name='order_create_config'),
    path('order_update_config/<int:pk>/', OrderConfigUpdateView.as_view(), name='order_update_config'),
    path('order_detail_view/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    path('checklist_create/<slug:tp>/<int:pk>', CheckListCreateView.as_view(), name='checklist_create'),
    path('checklist_config_update/<slug:tp>/<int:pk>', CheckListConfigUpdateView.as_view(), name='checklist_config_update'),
    path('checklist_sections_create/<slug:tp>/<int:pk>', CheckListSectionsCreateView.as_view(), name='checklist_sections_create'),

    path('checklist_detail/<slug:tp>/<int:pk>/', CheckListDetailView.as_view(), name='checklist_detail'),
    path('checklist_update/<slug:tp>/<int:pk>/', CheckListUpdateView.as_view(), name='checklist_update'),

    path('custom_login/', LoginView.as_view(), name='login'),

]
