from typing import Optional

from otk.models.otk_order import OTKOrder
from otk.services.services import create_order_config_section_entry, create_substation_type_entry_for_order_config


def get_config_section_from_order_id(order_id):
    """Возвращает секцию конфигурации по id OKTOrder"""
    order_entry = OTKOrder.objects.get(id=order_id)
    return order_entry.config_section


def create_order(order_num, type_sub) -> Optional[int]:
    """Создает заказ и добавляет к нему секцию конфигурации """
    section = create_order_config_section_entry('config')
    if section is None:
        return False

    substation_type = create_substation_type_entry_for_order_config('Тип подстанции', type_sub, section)
    if substation_type is None:
        return False

    try:
        order = OTKOrder(man_number=order_num, config_section=section)
        order.save()
    except Exception as e:
        print(e)
        return False

    return order.id
