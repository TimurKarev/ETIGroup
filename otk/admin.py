from django.contrib import admin
from otk.models.otk_order import OTKOrder, OrderConfigSection
from otk.models.tm_checklists import *
from otk.models.checklists import *


# Register your models here.
admin.site.register(OTKOrder)
admin.site.register(OrderConfigSection)

admin.site.register(TMCheckList)
admin.site.register(RM6CheckList)
admin.site.register(SKTMCheckList)
admin.site.register(SRTMCheckList)
admin.site.register(KTMUECheckList)
admin.site.register(YBPCheckList)
admin.site.register(SUCheckList)

admin.site.register(Checklist)
admin.site.register(ChListSection)
admin.site.register(StringPoint)
admin.site.register(IntegerPoint)

admin.site.register(FourChoicePoint)
admin.site.register(YesNoChoisePoint)
admin.site.register(SubstationTypePoint)