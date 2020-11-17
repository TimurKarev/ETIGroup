from django.db import models

class General(models.Model):
    name = models.CharField(max_length=100, 
                            default = '', 
                            blank = False)
    
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)

class Checklist(General):
    
    class Meta:
        db_table = 'checklist'


class ChListSection(General):
    checklist = models.ForeignKey(Checklist, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'chlistsection'
        

class SimplePoint(General):
    checklist = models.ForeignKey(ChListSection, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        abstract = True
    

class StringPoint(SimplePoint):
    string = models.CharField(max_length=100, default = '', blank = True)
    
    class Meta:
        db_table = 'string_point'

ELEMENT_CHOICES = (
    ('Не проверено', 'Не проверено'),
    ('Не используется','Не используется'),
    ('Принято', 'Принято'),
    ('Замечания','Замечания'),
)
class FourChoisePoint(SimplePoint):
    choise = models.CharField(max_length=15, 
                            choices = ELEMENT_CHOICES, 
                            default = 'Не проверено',
                            blank = False, 
                            null = False,
                            )

    comment = models.CharField(max_length=200, 
                                        default = '',
                                        verbose_name = 'Коментарий',
                                        blank = True)

    class Meta:
        db_table = 'fourchoisepoint'
    
    #TODO добавить заказ (???)
    # def __str__(self):
    #     return str(self.name)


PASSED_CHOICES = (
    ('НЕ принято', 'НЕ принято'),
    ("Принято", 'Принято'),
)
class YesNoChoisePoint(SimplePoint):
    choise = models.CharField(max_length=15,
                            choices = PASSED_CHOICES, 
                            default = 'НЕ принято',
                            blank = False, 
                            null = False,
                            )
    class Meta:
        db_table = 'yesnochoisepoint'