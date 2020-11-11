from django.db import models
from django.urls import reverse

ELEMENT_CHOICES = (
    ('Не проверено', 'Не проверено'),
    ('НЕ используется','Не используется'),
    ('Принято', 'Принято'),
    ('Замечания','Замечания'),
)

PASSED_CHOICES = (
    ('НЕ принято', 'НЕ принято'),
    ("Принято", 'Принято'),
)

# Create your models here.
class TMCheckList(models.Model):
    UE_Code = models.CharField(max_length=20, default = '', verbose_name = 'Шифр(УЭ)', blank = True)
    TM_Code = models.CharField(max_length=20, default = '', verbose_name = 'Шифр (ТМ)', blank = True)
    Type_KTM_UE = models.CharField(max_length=20, default = '', verbose_name = 'Тип КТМиУЭ', blank = True)
    Number_KTM_UE = models.CharField(max_length=20, default = '', verbose_name = 'зав. №', blank = True)
    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист телемеханики прошел все проверки')


    def get_absolute_url(self):
        return reverse('tm_checklist_detail', args=[str(self.id)])


class RM6CheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    serial = models.CharField(max_length=20, default = '', verbose_name = 'Заводской номер', blank = True)
    function = models.CharField(max_length=6, default = '', verbose_name = 'Состав функций', blank = True)
    cable_ts = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей ТС(правильность, маркировка')
    cable_wire = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей связи к клммам модуля связи (правильность, маркировка')
    wire_patch = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение патч-кордов от модуля связи к VIP, flair')
    cable_220 = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей питания ≈220 В VIP от ШСН')
    cable_24 = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей питания =24 В flair от КТМ')
    cable_earth = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'соединение экранов кабелей связи отдельных участков в единую цепь')
    earth_disable_RM6 = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'отсутствие заземления экранов в RM6')
    ts_rm6_controller = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'проверка прохождения ТС от RM6 до дискретных входов контроллера')
    ty_rm6_KTMUE = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'проверка прохождения ТУ от RM6 до КТМиУЭ')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист RM6 прошел все проверки')

class SKTMCheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    controller = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'контроллер')
    connections = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'автоматы, переключатели и предохранители согласно схеме')
    terminal_blocks = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'блоки клемм')
    UZIP = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'УЗИП')
    cable_24 = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'система питания =24В (в т.ч. предохранители в блоке батарей)')
    antenna_GPRS = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'антенна GPS')
    antenna_GSM = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'антенна GSM')
    antennas_bracket = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'кронштейны крепления антенн')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист ШКТМ прошел все проверки')
    

class SRTMCheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    creit = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'крейт расширения')
    connections = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'автоматы и предохранители согласно схеме')
    connections = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'автоматы и предохранители согласно схеме')
    terminal_blocks = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'блоки клемм')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист ШРТМ прошел все проверки')


class KTMUECheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    earth = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'наличие заземления шкафа ШКТМ, ШРТМ')
    inside_wire = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'выполнение внутришкафной разводки (полнота и правильность)')
    inside_earth = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'заземление оборудования шкафов (контроллер, розетка, УЗИП, система питания =24В)')
    marking = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'маркировка оборудования, проводов, клемм')
    outside_wire = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'правильность заводки кабеля в шкаф, крепление кабеля на рейке')
    wire_earth = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'заземление экранов кабелей связи')
    wire_marking = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей питания к клеммным блокам, маркировка жил')
    wire_ts_marking = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей ТС к клеммным блокам, маркировка жил')
    wire_ty_marking = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей ТУ к клеммным блокам, маркировка жил')
    wire_connect_marking = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей связи к клеммным блокам, маркировка жил')
    sleeve = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'наличие гильз на внешней стене для вывода на фасад кабелей антенн')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист КТМиУЭ прошел все проверки')

class YBPCheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    ts_connector = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение цепей ТС вводного выключателя')
    ts_disconnector = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение цепей ТС секционного разъединителя')
    tt = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'трансформаторы тока вводного выключателя (тип, номинал, класс точности, направление Л1-Л2)')
    wire_vv = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение измерительных цепей тока и напряжения ВВ(надежность подключения, маркировка, полярность И1-И2)')
    tt_earth_vv = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'заземление вторичных обмоток ТТ вводного выключателя')
    tt_lines = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'трансформаторы тока отходящих линий (тип, номинал, класс точности, направление Л1-Л2)')
    tt_number = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'Соответствие количества трансформаторов тока проекту')
    vire_ol = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение измерительных цепей тока и напряжения ОЛ(надежность подключения, маркировка, полярность И1-И2)')
    tt_earth_ol = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'заземление вторичных обмоток ТТ отходящих линий')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист УВР прошел все проверки')
    
class SUCheckList(models.Model):
    checklist = models.ForeignKey(TMCheckList, on_delete=models.CASCADE, null=True)
    py = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'ПУ - расположение тип напряжение, ток, дата поверки, маркировка')
    py_number = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'ПУ - количество')
    wire = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение измерительных цепей (правильность, маркировка, надежность)')
    test_block = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'испытательные колодки (количество+резерв, комплектность, правильность расключения, надежность крепления проводников, маркировка)')
    wire_reserve = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение цепей резервного питания')
    rs485_box = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'распределительные коробки RS485 (количество, комплектность)')
    wire_connection = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'подключение кабелей связи (расключение в РИ, подключение к ПУ, то-пология согласно структурной схеме, маркировка)')
    wire_helper = models.CharField(max_length=15, choices = ELEMENT_CHOICES, default = 'UNUSED', blank = False, null = False,
                                verbose_name = 'вспомогательные цепи (освещения, обогрева))')

    passed = models.CharField(max_length=15, choices = PASSED_CHOICES, default = 'NO', blank = False, null = False,
                                verbose_name = 'Чек лист ШУ прошел все проверки')