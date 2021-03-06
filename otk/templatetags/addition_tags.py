from django import template

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
  """
  Returns verbose_name for a field.
  """
  myinstance = eval(instance.split('.')[1].title())
  return myinstance._meta.get_field(field_name).verbose_name.title()


@register.filter(name='del_suffix')
def del_suffix(value : str):
  
    return value[:-3]


@register.filter
def index(indexable, i):
    return indexable[i]