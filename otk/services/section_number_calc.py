from otk.models.checklists import Checklist
from otk.models.otk_order import OTKOrder


class SectionNumberCalculator:
    DEFAULT_RETURN_VALUE = 1

    def __init__(
            self,
            order: OTKOrder,
            checklist_entry: Checklist,
            checklist_type: str,
    ):
        self._order_entry = order
        self._checklist_entry = checklist_entry
        self._checklist_type = checklist_type

        self._bottom_bm = None
        self._upper_bm = None

    @property
    def bottom_bm(self):
        if self._bottom_bm:
            return self._bottom_bm

        try:
            self._bottom_bm = self._checklist_entry.chlistsection_set.all() \
                .filter(name='config')[0] \
                .integerpoint_set.all() \
                .filter(name='Количество нижних модулей')[0] \
                .point_value
        except Exception as e:
            print(e)
            self._bottom_bm = self.DEFAULT_RETURN_VALUE

        return self._bottom_bm

    @property
    def upper_bm(self):
        if self._upper_bm:
            return self._upper_bm

        try:
            self._upper_bm = self._checklist_entry.chlistsection_set.all() \
                .filter(name='config')[0] \
                .integerpoint_set.all() \
                .filter(name='Количество верхних модулей')[0] \
                .point_value
        except Exception as e:
            print(e)
            self._upper_bm = self.DEFAULT_RETURN_VALUE

        return self._upper_bm

    def get_number(self, section_name):

        if section_name == 'Производство нижнего модуля' or \
                section_name == 'Металлоизделия нижний модуль' or \
                section_name == 'Размеры нижнего модуля' or \
                section_name == 'Проходные отверстия нижнего модуля' or \
                section_name == 'Отделочные работы нижнего модуля' or \
                section_name == 'Нижний модуль':
            return self.bottom_bm

        if section_name == 'Производство верхнего модуля' or \
                section_name == 'Металлоизделия верхнего модуля' or \
                section_name == 'Размеры верхнего модуля' or \
                section_name == 'Проходные отверстия верхнего модуля' or \
                section_name == 'Отделочные работы верхнего модуля' or \
                section_name == 'Верхний модуль':
            return self.upper_bm

        return self.DEFAULT_RETURN_VALUE
