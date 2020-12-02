import json
from typing import Optional

from pathlib import Path
import os

from otk.models.otk_order import OTKOrder, OrderConfigSection
from otk.models.checklists import *

from django.conf import settings

''' Создает чек лист телемеханики и добавляет его к номеру заказа 
    Возвращает id чеклиста'''


def create_checklist_by_checklist_type_from_json(
        order: OTKOrder,
        checklist_type: str,
        checklist_name: str
) -> Optional[int]:
    # # Проверяем, есть ли уже такой чеклист в базе
    # if is_checklist_exist(checklist_type, order):
    #     return None
    #
    # checklist_entry = create_checklist(name=checklist_name)
    checklist_entry = get_checklist_for_order_by_type(order, checklist_type)
    if checklist_entry is None:
        return None

    data = get_json_data(checklist_type)

    for section in data:
        if section['name'] == 'config':
            continue
        section_quantity = get_section_number(order, section['name'], checklist_type)

        for section_number in range(section_quantity):

            if section_quantity == 1:
                section_suffix = ''
            else:
                section_suffix = " - " + str(section_number + 1)

            section_entry = create_cl_section_entry(section['name'] + section_suffix, checklist_entry)
            if section_entry is None:
                continue

            for i, point in enumerate(section['points']):
                create_point_entry(point, i+1, section_entry)

    # Присщединение чеклиста к соответствующему полю Заказа
    try:
        if checklist_type == 'tm_checklist':
            order.tm_checklist = checklist_entry
            order.save()

        if checklist_type == 'el_checklist':
            order.el_checklist = checklist_entry
            order.save()

    except Exception as e:
        print(e)
        print('Error- order.save()')
        return None

    return checklist_entry.id


def get_section_number(order, section_name, checklist_type):
    """ Возвращает количество секций в чеклисте в зависимости от конфигурации заказа и чеклиста"""
    if checklist_type == 'tm_checklist':
        if section_name == 'Проверка RM6':
            return order.config_section.integerpoint_set \
                .all() \
                .get() \
                .point_value
    return 1


def is_checklist_exist(checklist_type, order) -> Optional[Checklist]:
    """Проверяет существует ли такой чеклист в базе
        возвращает:
            True - если существует
            False - если отсутствует
        """
    if checklist_type == 'bm_checklist' and order.bm_checklist is not None:
        return order.bm_checklist

    if checklist_type == 'el_checklist' and order.el_checklist is not None:
        return order.el_checklist

    if checklist_type == 'tm_checklist' and order.tm_checklist is not None:
        return order.tm_checklist

    if checklist_type == 'doc_checklist' and order.doc_checklist is not None:
        return order.doc_checklist

    if checklist_type == 'zip_checklist' and order.zip_checklist is not None:
        return order.zip_checklist

    if checklist_type == 'sal_checklist' and order.sal_checklist is not None:
        return order.sal_checklist

    return None


def create_checklist(name) -> Optional[Checklist]:
    """ Создает чеклист таблицу"""
    try:
        checklist_entry = Checklist(name=name)
        checklist_entry.save()
    except Exception as e:
        print(e)
        print('Error- create_bmchecklist_from_json -> checklist.save()')
        return None

    return checklist_entry


def create_cl_section_entry(name: str, key: Checklist) -> Optional[ChListSection]:
    """ Создает секцию чеклиста и добавляет ее к чеклисту"""
    try:
        section = ChListSection(name=name, checklist=key)
        section.save()
    except Exception as e:
        print(e, '- create_section_entry')
        return None
    return section


def create_order_config_section_entry(name: str) -> Optional[OrderConfigSection]:
    """ Создает секцию конфигурации заказа"""
    try:
        section = OrderConfigSection(name=name)
        section.save()
    except Exception as e:
        print(e, '- create_order_config_section_entry')
        return None
    return section


def create_point_entry(point, serial_number, section):
    if point['point_type'] == 'integer':
        create_integer_point_entry(
            point['name'],
            point['value'],
            serial_number,
            section)

    if point['point_type'] == 'string':
        create_string_point_entry(
            point['name'],
            serial_number,
            section)

    if point['point_type'] == 'four':
        create_four_point_entry(
            point['name'],
            serial_number,
            section)

    if point['point_type'] == 'yes':
        create_yes_no_entry(
            point['name'],
            serial_number,
            section)


def create_string_point_entry(
        name: str,
        serial_number,
        key,
        is_order_section: bool = False
) -> Optional[StringPoint]:
    """ Создает текстовой пункт и добавляет ее в секцию"""
    try:
        if is_order_section:
            string_point_entry = StringPoint(name=name, order_config=key)
        else:
            string_point_entry = StringPoint(name=name, checklist_section=key)

        string_point_entry.serial_number = serial_number
        string_point_entry.save()
    except Exception as e:
        print(e, '- create_string_point_entry')
        return None
    return string_point_entry


def create_four_point_entry(
        name: str,
        serial_number,
        key,
        is_order_section: bool = False
) -> Optional[FourChoicePoint]:
    """ Создает проверочный пункт и добавляет ее в секцию"""
    try:

        if is_order_section:
            four_point_entry = FourChoicePoint(name=name, order_config=key)
        else:
            four_point_entry = FourChoicePoint(name=name, checklist_section=key)
        four_point_entry.serial_number = serial_number
        four_point_entry.save()
    except Exception as e:
        print(e, '- create_four_point_entry')
        return None
    return four_point_entry


def create_yes_no_entry(name: str, serial_number, key: ChListSection, is_order_section: bool = False) -> Optional[
    YesNoChoicePoint]:
    """ Создает проверочный ДА/НЕТ пункт и добавляет ее в секцию"""
    try:
        if is_order_section:
            yes_no_point_entry = YesNoChoicePoint(name=name, order_config=key)
        else:
            yes_no_point_entry = YesNoChoicePoint(name=name, checklist_section=key)
        yes_no_point_entry.serial_number = serial_number
        yes_no_point_entry.save()
    except Exception as e:
        print(e, '- create_yes_no_entry')
        return None
    return yes_no_point_entry


def create_integer_point_entry(name: str, def_value, serial_number, key, is_order_section: bool = False):
    """ Создает числовой пункт и добавляет ее в секцию"""
    try:
        if is_order_section:
            integer_point_entry = IntegerPoint(name=name, order_config=key)
        else:
            integer_point_entry = IntegerPoint(name=name, checklist_section=key)
        integer_point_entry.point_value = def_value
        integer_point_entry.serial_number = serial_number
        integer_point_entry.save()
    except Exception as e:
        print(e, '- create_integer_point_entry')
        return None
    return integer_point_entry


def create_substation_type_entry_for_order_config(
        name: str,
        choice: str,
        key: OrderConfigSection
) -> Optional[SubstationTypePoint]:
    """Создает секцию конфигурации заказа"""
    try:
        substation_type_entry = SubstationTypePoint(name=name, point_value=choice, order_config=key)
        substation_type_entry.save()
    except Exception as e:
        print(e, '- substation_type_entry')
        return None
    return substation_type_entry


def get_json_data(string, config=False):
    """Возвращает заполненный объект из JSON в зависимости от типа чеклиста """
    STATIC_DIR = getattr(settings, "STATICFILES_DIRS", None)
    STATIC_DIR = STATIC_DIR[0]
    json_dir = os.path.join(STATIC_DIR, 'json')
    json_path = os.path.join(json_dir, string + '.json')

    try:
        with open(
                json_path,
                "r", encoding="utf-8"
        ) as read_file:
            data = json.load(read_file)
    except Exception as e:
        print(e)
        return None

    config_data = None
    if data[0]['name'] == 'config':
        config_data = data.pop(0)

    if config:
        return config_data
    else:
        return data


def get_checklist_name_by_type(tp, man_number):
    checklist_name = 'Чек лист'
    if tp == 'bm_checklist':
        checklist_name += ' строительной части'

    if tp == 'el_checklist':
        checklist_name += ' электрической части'

    return checklist_name + ', заказ №' + str(man_number)


def get_checklist_for_order_by_type(
        order_entry: OTKOrder,
        check_list_type: str,
        checklist_name: str = 'Чек лист',
):
    if check_list_type == 'bm_checklist':
        if order_entry.bm_checklist:
            return order_entry.bm_checklist
        else:
            checklist_entry = create_checklist(checklist_name)
            order_entry.bm_checklist = checklist_entry
            order_entry.save()
            return checklist_entry

    elif check_list_type == 'el_checklist':
        if order_entry.el_checklist:
            return order_entry.el_checklist
        else:
            checklist_entry = create_checklist(checklist_name)
            order_entry.el_checklist = checklist_entry
            order_entry.save()
            return checklist_entry

    return None
