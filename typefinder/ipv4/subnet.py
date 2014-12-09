# -*- coding: utf-8 -*-
import re

import ipaddress

from .. import generic

subnets =  [ipaddress.IPv4Network(u"0.0.0.0/%s" % cidr).netmask.exploded for cidr in range(0,33)]

import ip

def search(text):
    text = generic.clean(text)
    text = text.replace(',', ' ').replace('/', ' ')
    text = ' '.join(unicode(text).split()).replace(' - ', '-')
    subnets = []
    last_match = None
    for token in text.split():
        matches = re.findall(ip.ip_re, token, re.I)
        for match in matches:
            # An IP but not a subnet
            if not valid(match) and not last_match:
                last_match = match
            # A subnet not prefixed by an IP
            if not last_match and valid(match):
                last_match = None
                subnets.append(match)
    return subnets

def _clean(subnet):
    subnet = unicode(subnet)
    return subnet.replace(' ','')

def valid(subnet):
    subnet = _clean(subnet)
    if subnet not in subnets:
        return False
    return True

def clean(subnet):
    if valid(subnet):
        subnet = _clean(subnet)
        return subnet
    raise ValueError('\'{0}\' is not a valid IPv4 subnet mask'.format(subnet))
