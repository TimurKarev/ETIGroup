from django.db import models
from otk.models.checklists import Checklist, OrderConfigSection
from django.urls import reverse


# TODO Rename all models class names
class OTKOrder(models.Model):
    class Meta:
        db_table = 'otkorder'

    man_number = models.IntegerField(unique=True)

    tm_checklist = models.OneToOneField(Checklist,
                                        on_delete=models.SET_NULL,
                                        unique=True,
                                        blank=True,
                                        null=True,
                                        default=None)

    bm_checklist = models.OneToOneField(Checklist,
                                        on_delete=models.SET_NULL,
                                        unique=True,
                                        blank=True,
                                        null=True,
                                        default=None,
                                        related_name='bm_checklist')

    el_checklist = models.OneToOneField(Checklist,
                                        on_delete=models.SET_NULL,
                                        unique=True,
                                        blank=True,
                                        null=True,
                                        default=None,
                                        related_name='el_checklist')

    doc_checklist = models.OneToOneField(Checklist,
                                         on_delete=models.SET_NULL,
                                         unique=True,
                                         blank=True,
                                         null=True,
                                         default=None,
                                         related_name='doc_checklist')

    zip_checklist = models.OneToOneField(Checklist,
                                         on_delete=models.SET_NULL,
                                         unique=True,
                                         blank=True,
                                         null=True,
                                         default=None,
                                         related_name='zip_checklist')

    sal_checklist = models.OneToOneField(Checklist,
                                         on_delete=models.SET_NULL,
                                         unique=True,
                                         blank=True,
                                         null=True,
                                         default=None,
                                         related_name='sal_checklist')

    config_section = models.OneToOneField(OrderConfigSection,
                                          on_delete=models.SET_NULL,
                                          unique=True,
                                          blank=True,
                                          null=True,
                                          default=None,
                                          related_name='config_section')

    def __str__(self):
        return str(self.man_number)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
