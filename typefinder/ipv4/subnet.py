# -*- coding: utf-8 -*-
import re

import ipaddress

from .. import generic

import ip
import wildcard

what = 'ipv4.subnet'

def dump():
    """ Returns a list of all subnet masks """
    return wildcard.dump(_subnets=True)

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
    if subnet not in dump():
        return False
    return True

def clean(subnet):
    if valid(subnet):
        subnet = _clean(subnet)
        return subnet
    raise ValueError('\'{0}\' is not a valid IPv4 subnet mask'.format(subnet))
