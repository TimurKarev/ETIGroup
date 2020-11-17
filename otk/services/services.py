import json
from typing import Optional

from pathlib import Path
import os

from otk.models.order import OTKOrder
from otk.models.checklists import *

''' Создает чек лист телемеханики и добавляет его к номеру заказа 
    Возвращает id чеклиста'''
def create_tmchecklist_from_order_model(num_order: str) -> Optional[int]:
    
    try:
        tm_checklist = TMCheckList()
        tm_checklist.save()
    except:
        print('Error- create_tmchecklist_from_order_model -> tm_checklist.save()')
        return None

    try:
        tm_srtm = SRTMCheckList(checklist = tm_checklist)
        tm_srtm.save()
    except:
        print('Error- create_tmchecklist_from_order_model -> tm_srtm.save()')
        return None

    try:
        tm_sktm = SKTMCheckList(checklist = tm_checklist)
        tm_sktm.save()
    except:
        print('Error- create_tmchecklist_from_order_model -> tm_sktm.save()')
        return None

    try:
        tm_ktmue = KTMUECheckList(checklist = tm_checklist)
        tm_ktmue.save()
    except:
        print('Error- create_tmchecklist_from_order_model -> tm_ktmue.save()')
        return None
    
    order = OTKOrder.objects.get(id=num_order)
    rm_number = order.rm_number
    
    try:
        for i in range(rm_number):
            rm6_checklist = RM6CheckList(checklist = tm_checklist)
            rm6_checklist.save()
    except Exception as e:
        print(e + '\nError- create_tmchecklist_from_order_model -> rm6_checklist.save() iteration' + str(i))
        return None

    ybp_number = order.ybp_number
    try:
        for i in range(ybp_number):
            ybp_checklist = YBPCheckList(checklist = tm_checklist)
            ybp_checklist.save()
    except Exception as e:
        print(e + '\nError- create_tmchecklist_from_order_model -> ybp_checklist.save() iteration' + str(i))
        return None

    su_number = order.su_number
    try:
        for i in range(su_number):
            su_checklist = SUCheckList(checklist = tm_checklist)
            su_checklist.save()
    except Exception as e:
        print(e + '\nError- create_tmchecklist_from_order_model -> su_checklist.save() iteration' + str(i))
        return None

    try:
        order.tm_checklist = tm_checklist
        order.save()
    except Exception as e:
        print(e + '\nError- create_tmchecklist_from_order_model -> order.save() iteration' + str(i))
        return None

    return tm_checklist.id if tm_checklist else None

def create_bmchecklist_from_json(order: OTKOrder) -> Optional[int]:

    if order.bm_checklist is not None:
        return None
    
    checklist_entry = create_checklist(name = 'Строительная часть заказ №' + str(order.man_number))
    if checklist_entry is None:
        return None

    #TODO вынести в отдельный функцию придумать фабрику
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    JSON_DIR = Path('static/json/bm_checklist.json')
    with open(os.path.join(BASE_DIR, JSON_DIR), 
                "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    ######################################################

    for section in data['sections']:
        section_entry = create_section_entry(section['name'], checklist_entry)
        if section_entry is not None:
            for four_point in section['four_points']:
                create_four_point_entry(four_point, section_entry)
            create_yes_no_entry(section['yes_no'], section_entry)
    
    try:
        order.bm_checklist = checklist_entry
        order.save()
    except Exception as e:
        print(e)
        print('Error- order.save()')
        return None
    
    return checklist_entry.id



''' Создает чеклист'''
def create_checklist(name) -> Optional[Checklist]:
    
    try:
        checklist_entry = Checklist(name = name)
        checklist_entry.save()
    except Exception as e:
        print(e)
        print('Error- create_bmchecklist_from_json -> checklist.save()')
        return None

    return checklist_entry

''' Создает секцию чеклиста и добавляет ее к чеклисту'''
def create_section_entry(name: str, key) -> Optional[ChListSection]:
    try:
        section = ChListSection(name = name, checklist = key)
        section.save()
    except Exception as e:
        print(e, '- create_section_entry')
        return None
    return section


''' Создает проверочный пункт и добавляет ее в секцию'''
def create_four_point_entry(name: str, key: ChListSection) -> Optional[FourChoisePoint]:
    try:
        four_point_entry = FourChoisePoint(name = name, checklist = key)
        four_point_entry.save()
    except Exception as e:
        print(e, '- create_four_point_entry')
        return None
    return four_point_entry


''' Создает проверочный ДА/НЕТ пункт и добавляет ее в секцию'''
def create_yes_no_entry(name: str, key: ChListSection) -> Optional[YesNoChoisePoint]:
    try:
        yes_no_point_entry = YesNoChoisePoint(name = name, checklist = key)
        yes_no_point_entry.save()
    except Exception as e:
        print(e, '- create_yes_no_entry')
        return None
    return yes_no_point_entry