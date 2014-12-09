# -*- coding: utf-8 -*-
import re
import math

import ipaddress

from .. import generic

import ip

def dump(_subnets=False):
    """ Returns a list of all wildcard masks """
    wildcard_ints = [int(math.pow(2, i)) - 1 for i in range(0, 33)]
    wildcard = list()
    for wildard_int in wildcard_ints:
        wc = bin(wildard_int).replace('0b', '').zfill(32)
        if _subnets:
            wc = wc[::-1]
        wc = [str(int(x, 2)) for x in re.split(r'([01]{8})', wc) if x]
        wildcard.append('.'.join(wc))
    return wildcard

def search(text):
    text = generic.clean(text)
    text = text.replace(',', ' ').replace('/', ' ').replace(' - ', '-')
    wildcards = []
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
                wildcards.append(match)
    return wildcards

def _clean(wildcard):
    wildcard = unicode(wildcard)
    return wildcard.replace(' ','')

def valid(wildcard):
    wildcard = _clean(wildcard)
    if wildcard not in dump():
        return False
    return True

def clean(wildcard):
    if not valid(wildcard):
        raise ValueError('\'{0}\' is not a valid IPv4 wildcard mask'.format(wildcard))
    wildcard = _clean(wildcard)
    return wildcard
