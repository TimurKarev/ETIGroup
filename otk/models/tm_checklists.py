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


class RM6CheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    serial = models.CharField(max_length=20, default = '', verbose_name = 'Заводской номер', blank = True)


class OneMoreTables(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    serial = models.CharField(max_length=20, default = '', verbose_name = 'Заводской номер', blank = True)