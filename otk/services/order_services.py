from otk.models.otk_order import OTKOrder
from otk.views.forms.model_forms import StringPointForm, IntegerPointForm


def get_config_section_from_order_id(order_id):
    order_entry = OTKOrder.objects.get(id=order_id)
    return order_entry.config_section


def get_section_context(section, data=None):
    all_points_entries = []

    for i, p in enumerate(section.stringpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": StringPointForm(instance=p, data=data, prefix='s'+str(i))
            }
        )

    for i, p in enumerate(section.integerpoint_set.all()):
        all_points_entries.append(
            {
                "serial_number": p.serial_number,
                "name": p.name,
                "value": p.point_value,
                "form": IntegerPointForm(instance=p, data=data, prefix='i'+str(i))
            }
        )

    # for p in section.yesnochoicepoint_set.all():
    #     all_points_entries.append(p)
    #
    # for p in section.fourchoicepoint_set.all():
    #     all_points_entries.append(p)

    all_points_entries = sorted(all_points_entries, key=lambda i: i['serial_number'])
#    print(all_points_entries)

    return all_points_entries
