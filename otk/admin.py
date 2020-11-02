from django.contrib import admin
from otk.models.order import OTKOrder
from otk.models.tm_checklists import TMCheckList
from otk.models.tm_checklists import RM6CheckList
from otk.models.tm_checklists import OneMoreTables


# Register your models here.
admin.site.register(TMCheckList)
admin.site.register(OTKOrder)
admin.site.register(RM6CheckList)
admin.site.register(OneMoreTables)