# -*- coding: utf-8 -*-
import re

import ipaddress

from .. import generic
import subnet, wildcard, ip_range

ip_re = r'(?<![0-9/-])(?:(?:\d+\.){3}\d+)(?![0-9/-])'

what = 'ipv4.ip_range'

def search(text):
    text = generic.clean(text)
    text = text.replace(' - ', '-')
    text = text.replace(' / ', '/')
    text = generic.remove_type(text, ip_range)
    ips = []
    last_match = None
    for token in text.split():
        if valid(token):
            if last_match:
                ips.append(clean(last_match))    
            last_match = token
        else:
            if subnet.valid(token) or wildcard.valid(token):
                last_match = None
    if last_match:
        ips.append(clean(last_match))
    return ips

def _clean(ip):
    return generic.clean(ip)
    

def valid(ip):
    ip = _clean(ip)
    if subnet.valid(ip):
        return False
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        return False
    return True

def clean(ip):
    if not valid(ip):
        raise ValueError('\'{0}\' is not a valid IPv4 address'.format(ip))
    ip = _clean(ip)
    return ipaddress.IPv4Address(ip).exploded
