import datetime
from django import template

register = template.Library()

@register.simple_tag
def numero_ano(numero, ano):
    return f"{numero}/{ano}"
