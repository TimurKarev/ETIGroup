from django import template

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
  """
  Returns verbose_name for a field.
  """
  myinstance = eval(instance.split('.')[1].title())
  return myinstance._meta.get_field(field_name).verbose_name.title()