# -*- coding: utf-8 -*-

from .. import generic

def search(text):
    floating_point = list()
    text = ' '.join(unicode(text).split()).strip(',')
    for token in text.split():
        if valid(token):
            floating_point.append(clean(token))
    return floating_point

def valid(number):
    try:
        number = float(number)
    except ValueError:
        return False
    return not number.is_integer()

def clean(number):
    if valid(number):
        return float(number)
    raise ValueError('{0} is not a floating point'.format(number))
