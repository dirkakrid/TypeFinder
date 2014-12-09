# -*- coding: utf-8 -*-
import re

import ipaddress

import ip
from plan.types import generic

def _invalid(ip_range):
    raise ValueError('\'{0}\' is not a valid IPv4 address range'.format(ip_range))

def _clean(ip_range):
    ip_range = unicode(ip_range)
    ip_range = ip_range.replace(' ', '')
    return ip_range.split('-')

def get_network(network_range):
    """ Given a range, return the smallest possible network that contains it """
    low, high = network_range.strip().split("-")
    high = ipaddress.IPv4Address(unicode(high))
    for prefix in reversed(range(33)):
        low_network = ipaddress.IPv4Interface(unicode('{0}/{1}'.format(low, prefix)))
        low_network = low_network.network
        if high in low_network:
            return low_network.exploded
    return False

def search(text):
    text = generic.clean(text)
    matches = re.findall('(?:\d+\.){3}\d+\s*-\s*(?:\d+\.){3}\d+', text, re.I)
    ip_ranges = list()
    for match in matches:
        if valid(match):
            ip_ranges.append(clean(match))
    return ip_ranges

def valid(ip_range):
    try:
        first, second = _clean(ip_range)
    except ValueError:
        return False
    if ip.valid(first) and ip.valid(second) and ip.clean(first) != ip.clean(second):
        return True
    return False

def clean(ip_range):
    if not valid(ip_range):
        _invalid(ip_range)    
    first, second = _clean(ip_range)
    first = ipaddress.IPv4Address(first)
    second = ipaddress.IPv4Address(second)
    low = first
    high = second
    if first > second:
        low = second
        high = first
    return u'-'.join([low.exploded, high.exploded])
