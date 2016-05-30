
import datetime
from django import template

register = template.Library()


@register.simple_tag
def Eligible(user):

    if datetime.date.today().year - user.date_of_birth.year >= 13:
        return 'allowed'
    return 'blocked'


@register.simple_tag
def BizzFuzz(user):

    if not user.random % 15:
        return 'BizzFuzz'

    if not user.random % 5:
        return 'Fuzz'

    if not user.random % 3:
        return 'Bizz'

    return str(user.random)
