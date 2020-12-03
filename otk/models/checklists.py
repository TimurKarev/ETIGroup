from django.db import models

from django.utils.translation import gettext_lazy as _


class General(models.Model):
    name = models.CharField(max_length=100,
                            default='',
                            blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class Checklist(General):
    class Meta:
        db_table = 'checklist'


class OrderConfigSection(General):
    class Meta:
        db_table = 'orderconfigsection'


class ChListSection(General):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'chlistsection'


class SimplePoint(General):
    checklist_section = models.ForeignKey(ChListSection, on_delete=models.CASCADE, null=True)
    order_config = models.ForeignKey(OrderConfigSection, on_delete=models.CASCADE, null=True)

    serial_number = models.IntegerField(default=0, blank=True)

    class Meta:
        abstract = True


class StringPoint(SimplePoint):
    point_value = models.CharField(max_length=100, default='', blank=True)

    class Meta:
        db_table = 'stringpoint'


class IntegerPoint(SimplePoint):
    point_value = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'integerpoint'


class FourChoicePoint(SimplePoint):
    class Four(models.TextChoices):
        UNCHECKED = 'Не проверено', _('Не проверено')
        UNUSED = 'Не используется', _('Не используется')
        APPROVED = 'Принято', _('Принято')
        COMMENT = 'Коментарий', _('Коментарий')

    point_value = models.CharField(max_length=15,
                                   choices=Four.choices,
                                   default=Four.UNCHECKED,
                                   blank=False,
                                   null=False,
                                   )

    comment = models.CharField(max_length=200,
                               default='',
                               verbose_name='Коментарий',
                               blank=True)

    class Meta:
        db_table = 'fourchoicepoint'

    # TODO добавить заказ (???)
    # def __str__(self):
    #     return str(self.name)


class YesNoChoicePoint(SimplePoint):
    class YesNo(models.TextChoices):
        YES = 'Пройдены', _('Пройдены')
        NO = 'Не Пройдены', _('Не Пройдены')

    point_value = models.CharField(max_length=15,
                                   choices=YesNo.choices,
                                   default=YesNo.NO,
                                   blank=False,
                                   null=False,
                                   )

    class Meta:
        db_table = 'yesnochoicepoint'


class SubstationTypePoint(SimplePoint):
    class SunType(models.TextChoices):
        BKTP = 'БКТП', _('БКТП')

    point_value = models.CharField(max_length=15,
                                   choices=SunType.choices,
                                   default=SunType.BKTP,
                                   blank=False,
                                   null=False,
                                   )

    class Meta:
        db_table = 'substationtypepoint'
