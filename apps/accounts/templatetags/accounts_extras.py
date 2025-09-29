from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Filtro de plantilla para añadir una clase CSS a un campo de formulario.

    Uso en la plantilla:
    {{ form.field|add_class:"clase-css-a-anadir" }}
    """
    return value.as_widget(attrs={'class': arg})