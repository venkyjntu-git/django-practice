import random
from django import template
register = template.Library()

@register.simple_tag
def random_int(a,b):
    #print("call  ",st)
    return random.randint(a,b)
