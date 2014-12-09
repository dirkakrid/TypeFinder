# -*- coding: utf-8 -*-
import re
from datetime import datetime

from ..configuration import Configuration

import generic

_time_formats = Configuration.search_date_formats
_standard_format = Configuration.standard_date_format

_date_re = r'\d+\s+\d+\s+\d+'

def search(text):
    text = generic.clean(text)
    dates = list()
    for token in text.split():
        token = token.lower().strip('.,')
        if valid(token):
            token = clean(token)
            dates.append(token)
    for token in re.findall(_date_re, text, re.I):
        if valid(token):
            token = clean(token)
            dates.append(token)
    return dates

def _clean(date):
    date_object = None
    for time_format in _time_formats:
        try:
            date_object = datetime.strptime(date, time_format)
            break
        except (ValueError, TypeError):
            date_object = None
    if not date_object:
        raise ValueError('{0} is not a valid date'.format(date))
    return date_object.strftime(_standard_format)

def valid(date):
    try:
        _clean(date)
    except ValueError:
        return False    
    return True

def clean(date):
    if valid(date):
        return _clean(date)
    raise ValueError('\'{0}\' is not a valid date'.format(date))
