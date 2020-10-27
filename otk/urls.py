from django.urls import path
from .views import CheckListListView, CkeckListDetailView, CheckListListCreate, CheckListListEdit

urlpatterns = [
    path('', CheckListListView.as_view(), name='checklist_list'),
    path('checklist/<int:pk>/', CkeckListDetailView.as_view(), name='checklist_detail'),
    path('checklist/new', CheckListListCreate.as_view(), name='checklist_new'),
    path('checklist/<int:pk>/edit', CheckListListEdit.as_view(), name='checklist_edit'),
]
