# -*- coding: utf-8 -*-

from .. import generic

def search(text):
    integers = list()
    text = ' '.join(unicode(text).split()).strip(',')
    for token in text.split():
        if valid(token):
            integers.append(clean(token))
    return integers

def valid(number):
    try:
        number = float(number)
    except ValueError:
        return False
    return number.is_integer()

def clean(number):
    if valid(number):
        return int(float(number))
    raise ValueError('{0} is not an integer'.format(number))
