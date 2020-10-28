from django.contrib import admin
from otk.models.tm_checklists import TMCheckList
from otk.models.order import OTKOrder

# Register your models here.
admin.site.register(TMCheckList)
admin.site.register(OTKOrder)