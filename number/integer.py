# -*- coding: utf-8 -*-

def valid(number):
    try:
        number = float(number)
    except ValueError:
        return False
    return number.is_integer()

def clean(number):
    if valid(number):
        return int(number)
    raise ValueError('{0} is not an integer'.format(number))
