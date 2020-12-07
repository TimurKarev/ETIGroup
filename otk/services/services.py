import json
from typing import Optional

import os

from otk.models.checklists import Checklist
from otk.models.otk_order import OTKOrder
from otk.models.checklists import *

from django.conf import settings

from otk.services.section_number_calc import SectionNumberCalculator
from otk.views.forms.model_forms import StringPointForm, IntegerPointForm, YesNoChoicePointForm, FourChoicePointForm


def is_checklist_have_several_sections(checklist_entry):
    """Проверяет имеет ли чеклист какие-нибудь секции кроме конфиг"""
    sections = checklist_entry.chlistsection_set.all()
    if len(sections) > 1 \
            or (len(sections) == 1 and sections[0].name != 'config'):
        return True
    return False


def create_checklist_by_checklist_type_from_json(
        order: OTKOrder,
        checklist_type: str,
        checklist_name: str
) -> Optional[int]:
    """ Создает чек лист телемеханики и добавляет его к номеру заказа
        Возвращает id чеклиста"""
    checklist_entry = get_checklist_for_order_by_type(order, checklist_type, checklist_name)
    if checklist_entry is None:
        return None

    # TODO сделать проверку на конфиг секцию, сделать уникальные номера и системму назначений уникальных config-имен
    if is_checklist_have_several_sections(checklist_entry):
        return checklist_entry.id

    data = get_json_data(checklist_type)

    section_calc = SectionNumberCalculator(order, checklist_entry, checklist_type)

    for section in data:
        if section['name'] == 'config':
            continue
        section_quantity = section_calc.get_number(section['name'])

        for section_number in range(section_quantity):

            if section_quantity == 1:
                section_suffix = ''
            else:
                section_suffix = " - " + str(section_number + 1)

            section_entry = create_cl_section_entry(section['name'] + section_suffix, checklist_entry)
            if section_entry is None:
                continue

            for i, point in enumerate(section['points']):
                create_point_entry(point, i + 1, section_entry)

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


def get_order_by_checklist(checklist_entry, checklist_type):
    try:
        if checklist_type == 'bm_checklist':
            return checklist_entry.bm_checklist

    except Exception as e:
        print(e)
        return None


def get_section_context(section, data=None, section_prefix='sec', form=True):
    """Возвращает дату из модели"""
    section_dict = {'name': section.name}
    all_points_entries = []

    for i, p in enumerate(section.stringpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": None if not form else StringPointForm(
                    instance=p,
                    data=data,
                    prefix='s' + str(i) + str(section_prefix)
                )
            }
        )

    for i, p in enumerate(section.integerpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": None if not form else IntegerPointForm(
                    instance=p,
                    data=data,
                    prefix='i' + str(i) + str(section_prefix)
                )
            }
        )

    for i, p in enumerate(section.yesnochoicepoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": None if not form else YesNoChoicePointForm(
                    instance=p,
                    data=data,
                    prefix='y' + str(i) + str(section_prefix)
                )
            }
        )

    for i, p in enumerate(section.fourchoicepoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "comment": p.comment,
                "form": None if not form else FourChoicePointForm(
                    instance=p,
                    data=data,
                    prefix='f' + str(i) + str(section_prefix)
                )
            }
        )

    all_points_entries = sorted(all_points_entries, key=lambda serial: serial['serial_number'])

    section_dict['points'] = all_points_entries
    return section_dict


def get_detail_context_from_checklist_object(checklist_object, post_data=None, form=True) -> Optional[list]:
    """Возвращает список сущностей для присоединения к context в DetailView
        для конкретного чеклиста"""
    sections = checklist_object.chlistsection_set.all()
    data = []
    for i, section in enumerate(sections):
        if section.name == 'config':
            continue
        data.append(get_section_context(section, data=post_data, section_prefix='sec' + str(i), form=form))

    return data


def update_yesno_fields(checklist_entry: Checklist):
    """Подчитывает значение поля Принято/Непринято и обновляет соответствующее поле"""
    sections = checklist_entry.chlistsection_set.all()
    for section in sections:
        yesno_points = section.yesnochoicepoint_set.all()
        if len(yesno_points) > 0:
            yesno_point = yesno_points[0]
            # print(yesno_point, "  ---- ",  section.name)
            four_points = section.fourchoicepoint_set.all()
            is_no_value = False
            for four_point in four_points:
                if four_point.point_value == four_point.Four.UNCHECKED or \
                        four_point.point_value == four_point.Four.COMMENT:
                    is_no_value = True
                    try:
                        yesno_point.point_value = yesno_point.YesNo.NO
                        yesno_point.save()
                        break
                    except Exception as e:
                        print(e)

            if not is_no_value:
                try:
                    yesno_point.point_value = yesno_point.YesNo.YES
                    yesno_point.save()
                except Exception as e:
                    print(e)


def get_config_data_by_type(tp):
    """Возвращает секцию 'config' в виде словаря"""
    config_data = get_json_data(tp, True)
    return config_data


def create_config_section_by_data(checklist, config_data):
    """Создает секцию config для чеклиста по словарю"""
    existing_sections = checklist.chlistsection_set.all()
    config_section = None
    if len(existing_sections) > 0:
        config_section = existing_sections.filter(name='config')[0]

    if config_section is not None:
        return config_section.id

    config_section = create_cl_section_entry('config', checklist)
    if config_section is None:
        return None

    for i, point in enumerate(config_data['points']):
        create_point_entry(point, i + 1, config_section)

    return config_section.id
