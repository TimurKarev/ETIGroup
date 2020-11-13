from typing import Optional

from otk.models.order import OTKOrder
from otk.models.tm_checklists import *

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
