# -*- coding: utf-8 -*-
import ipaddress

def valid(network):
    try:
        ipaddress.IPv6Network(unicode(network))
    except ipaddress.AddressValueError:
        return False
    return True

def clean(network):
    if not valid(network):
        raise ValueError('\'{0}\' is not a valid IPv6 network'.format(network))
    return ipaddress.IPv6Network(unicode(network)).exploded
