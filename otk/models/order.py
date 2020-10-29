from django.db import models
from otk.models.tm_checklists import *

class OTKOrder(models.Model):
    man_number = models.IntegerField()
    tm_checklist = models.OneToOneField(TMCheckList, on_delete=models.CASCADE, blank = True, null = True, default = None)
    
    def __str__(self):
        return str(self.man_number)