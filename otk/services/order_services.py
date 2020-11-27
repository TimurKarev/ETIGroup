from otk.models.otk_order import OTKOrder
from otk.views.forms.model_forms import (
                                         StringPointForm,
                                         IntegerPointForm,
                                         FourChoicePointForm,
                                         YesNoChoicePointForm
                                        )


def get_config_section_from_order_id(order_id):
    """Возвращает секцию конфигурации по id OKTOrder"""
    order_entry = OTKOrder.objects.get(id=order_id)
    return order_entry.config_section


def get_section_context(section, data=None, section_prefix='sec'):
    all_points_entries = []

    for i, p in enumerate(section.stringpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": StringPointForm(
                                        instance=p,
                                        data=data,
                                        prefix='s'+str(i)+str(section_prefix)
                                        )
            }
        )

    for i, p in enumerate(section.integerpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": IntegerPointForm(
                                        instance=p,
                                        data=data,
                                        prefix='i'+str(i)+str(section_prefix)
                                       )
            }
        )

    for i, p in enumerate(section.yesnochoicepoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": YesNoChoicePointForm(
                                            instance=p,
                                            data=data,
                                            prefix='y' + str(i)+str(section_prefix)
                                            )
            }
        )

    for i, p in enumerate(section.fourchoicepoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": FourChoicePointForm(
                                            instance=p,
                                            data=data,
                                            prefix='f' + str(i)+str(section_prefix)
                                            )
            }
        )

    all_points_entries = sorted(all_points_entries, key=lambda serial: serial['serial_number'])

    return all_points_entries
