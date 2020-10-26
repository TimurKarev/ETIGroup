from django.urls import path
from .views import CheckListListView

urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),
]
