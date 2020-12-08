from django.contrib import admin
from otk.models.otk_order import OTKOrder
from otk.models.checklists import *


# Register your models here.
admin.site.register(OTKOrder)
admin.site.register(OrderConfigSection)

admin.site.register(Checklist)
admin.site.register(ChListSection)
admin.site.register(StringPoint)
admin.site.register(IntegerPoint)

admin.site.register(FourChoicePoint)
admin.site.register(YesNoChoicePoint)
admin.site.register(SubstationTypePoint)