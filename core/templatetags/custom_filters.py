from django import template

register = template.Library()

@register.filter
def div(value, divisor):
    try:
        return value // divisor
    except (ZeroDivisionError, TypeError):
        return 0
    

@register.filter
def batch(iterable, n):
    """
    Divide una lista en grupos de tamaño n.
    Ejemplo: [1, 2, 3, 4, 5] | batch:3 -> [[1, 2, 3], [4, 5]]
    """
    length = len(iterable)
    for i in range(0, length, n):
        yield iterable[i:i + n]