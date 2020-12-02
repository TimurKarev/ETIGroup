from otk.models.checklists import Checklist
from otk.models.otk_order import OTKOrder


class SectionNumberCalculator:

    def __init__(
            self,
            order: OTKOrder,
            checklist_entry: Checklist,
            checklist_type: str,
    ):
        self.order_entry = order
        self.checklist_entry = checklist_entry
        self.checklist_type = checklist_type

        self.bottom_bm = None
        self.upper_bm = None

    def _init_bm_variables(self):
        try:
            self.bottom_bm = self.checklist_entry.chlistsection_set.all() \
                    .filter(name='config')[0] \
                    .integerpoint_set.all() \
                    .filter(name='Количество нижних модулей')[0] \
                    .point_value
        except Exception as e:
            print(e)
            self.bottom_bm = 1

        try:
            self.upper_bm = self.checklist_entry.chlistsection_set.all() \
                    .filter(name='config')[0] \
                    .integerpoint_set.all() \
                    .filter(name='Количество верхних модулей')[0] \
                    .point_value
        except Exception as e:
            print(e)
            self.upper_bm = 1


def tm_checklist_number(order, section_name):
    if section_name == 'Проверка RM6':
        return order.config_section.integerpoint_set \
            .all() \
            .get() \
            .point_value


def bm_checklist_number(checklist_entry, section_name):
    if section_name == 'Производство нижнего модуля':
        try:
            sections = checklist_entry.chlistsection_set.all()
            section = sections.filter(name='config')[0]
            int_points_num = section.integerpoint_set.all()
            nm_point = int_points_num.filter(name='Количество нижних модулей')[0]
            num = nm_point.point_value
            return num
        except Exception as e:
            print(e)
            return 1

    return 1


def get_section_number(order, checklist_entry, section_name, checklist_type):
    """ Возвращает количество секций в чеклисте в зависимости от конфигурации заказа и чеклиста"""
    if checklist_type == 'tm_checklist':
        return tm_checklist_number(order, section_name)

    if checklist_type == 'bm_checklist':
        return bm_checklist_number(checklist_entry, section_name)

    return 1
