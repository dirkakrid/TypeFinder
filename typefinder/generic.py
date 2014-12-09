# -*- coding: utf-8 -*-

def clean(text):
    return ' '.join(unicode(text).split()).strip('.,')

def remove_type(text, the_type):
    """ Remove from the text any valid token of the given type """
    for token in text.split():
        if the_type.valid(token):
            text = text.replace(token, '')
    text = ' '.join(text.split())
    return text
