from . import register


@register.inclusion_tag('utils/_form_field.html')
def form_field(field):
    return {'field': field}
