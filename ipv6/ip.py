# -*- coding: utf-8 -*-
import ipaddress

def valid(ip):
    ip = unicode(ip)
    try:
        ipaddress.IPv6Address(ip)
    except ipaddress.AddressValueError:
        return False
    return True

def clean(ip):
    if not valid(ip):
        raise ValueError('\'{0}\' is not a valid IPv6 address'.format(ip))
    return ipaddress.IPv6Address(unicode(ip)).exploded
