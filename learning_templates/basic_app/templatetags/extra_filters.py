from django import template

register = template.Library()

def cut(value, arg):
    """ Cuts out all the values of 'arg' from the string!"""
    return value.replace(arg, '')

def lower_case(value):
    """Returns the string in lowercase"""
    return value.lower()

register.filter('cut', cut)
register.filter('lowercase', lower_case)
