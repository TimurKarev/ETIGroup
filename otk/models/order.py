from django.db import models
from otk.models.tm_checklists import TMCheckList
from otk.models.checklists import Checklist
from django.urls import reverse

SUBSTATION_TYPE_CHOICES = (
    ('БКТП', 'БКТП'),
)

#TODO Rename all models class names
class OTKOrder(models.Model):
    man_number = models.IntegerField(unique=True)
    
    tm_checklist = models.OneToOneField(TMCheckList, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None)

    bm_checklist = models.OneToOneField(Checklist, 
                                        on_delete=models.SET_NULL,
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None,
                                        related_name = 'bm_checklist')

    el_checklist = models.OneToOneField(Checklist, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None,
                                        related_name = 'el_checklist')

    doc_checklist = models.OneToOneField(Checklist, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None,
                                        related_name = 'doc_checklist')

    zip_checklist = models.OneToOneField(Checklist, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None,
                                        related_name = 'zip_checklist')

    sal_checklist = models.OneToOneField(Checklist, 
                                        on_delete=models.SET_NULL, 
                                        unique=True,
                                        blank = True, 
                                        null = True, 
                                        default = None,
                                        related_name = 'sal_checklist')


    substation_type = models.CharField(max_length=15, 
                                        choices = SUBSTATION_TYPE_CHOICES,
                                        default = 'БКТП',
                                        blank = False, 
                                        null = False,
                                        verbose_name = 'Тип подстанции')
    
    rm_number = models.IntegerField(unique=False, default=4)
    ybp_number = models.IntegerField(unique=False, default=2)
    su_number = models.IntegerField(unique=False, default=2)
    
    def __str__(self):
        return str(self.man_number)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])