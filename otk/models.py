from django.db import models

ELEMENT_CHOICES = (
    ('NOT_TESTED', 'Не проверено'),
    ('UNUSED','Не используется'),
    ('ACCEPTED', 'Принято'),
    ('DECLINE','Замечания'),
)

# Create your models here.
class TMCheckList(models.Model):
    man_number = models.CharField(max_length=200)
    
    Code_UE = models.CharField(max_length=10, blank=True)
    Code_TM = models.CharField(max_length=10, blank=True)
    Type_KTM_UE = models.CharField(max_length=10, blank=True)
    Number_KTM_UE = models.CharField(max_length=10, blank=True)
    
    SKTM = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='UNUSED')
    SKTM_kontroller = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_commutations = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_klemmas_blocks = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_UZIP = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_supply = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_GSM_antenna = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_GSM_antenna = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_antennas_bracket = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')
    SKTM_crait = models.CharField(max_length=10, choices=ELEMENT_CHOICES, default='NOT_TESTED')

    def __str__(self):
        return self.man_number