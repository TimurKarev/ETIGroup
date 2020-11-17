from django.contrib import admin
from otk.models.order import OTKOrder
from otk.models.tm_checklists import *
from otk.models.checklists import *


# Register your models here.
admin.site.register(OTKOrder)

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
admin.site.register(FourChoisePoint)
admin.site.register(YseNoChoisePoint)