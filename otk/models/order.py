from django.db import models
from otk.models.tm_checklists import TMCheckList

SUBSTATION_TYPE_CHOICES = (
    ('БКТП', 'БКТП'),
)

class OTKOrder(models.Model):
    man_number = models.IntegerField(unique=True)
    
    tm_checklist = models.OneToOneField(TMCheckList, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None)
    
    substation_type = models.CharField(max_length=15, 
                                        choices = SUBSTATION_TYPE_CHOICES,
                                        default = 'БКТП',
                                        blank = False, 
                                        null = False,
                                        verbose_name = 'Тип подстанции')
    
    rm_number = models.IntegerField(unique=True, default=4)
    ybp_number = models.IntegerField(unique=True, default=2)
    su_number = models.IntegerField(unique=True, default=2)
    
    def __str__(self):
        return str(self.man_number)