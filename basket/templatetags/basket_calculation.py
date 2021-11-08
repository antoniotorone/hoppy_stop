from django import template


register = template.Library()


@register.filter(name='calc_gross')
def calc_gross(price, quantity):
    return float(price) * int(quantity)
