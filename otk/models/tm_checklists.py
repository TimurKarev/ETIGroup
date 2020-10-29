from django.db import models
from django.urls import reverse

ELEMENT_CHOICES = (
    ('NOT_TESTED', 'Не проверено'),
    ('UNUSED','Не используется'),
    ('ACCEPTED', 'Принято'),
    ('DECLINE','Замечания'),
)

# Create your models here.
class TMCheckList(models.Model):
    UE_Code = models.CharField(max_length=20, default = '', verbose_name = 'Шифр(УЭ)', blank = True)
    TM_Code = models.CharField(max_length=20, default = '', verbose_name = 'Шифр (ТМ)', blank = True)
    Type_KTM_UE = models.CharField(max_length=20, default = '', verbose_name = 'Тип КТМиУЭ', blank = True)
    Number_KTM_UE = models.CharField(max_length=20, default = '', verbose_name = 'зав. №', blank = True)
    
    
    # def __str__(self):
    #     return self.
    
    # def get_absolute_url(self):
    #     return reverse("checklist_detail", args=[str(self.id)])

