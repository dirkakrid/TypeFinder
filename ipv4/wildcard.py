# -*- coding: utf-8 -*-
import re
import ipaddress

from subnet import subnets
from plan.types import generic

import ip

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

wildcards = []
for subnet in subnets:
    binary = bin(int(ipaddress.IPv4Address(subnet))).replace('0b','')
    flipped = binary[::-1]
    wildcard = ipaddress.IPv4Address(int(flipped, 2)).exploded
    wildcards.append(wildcard)

def _clean(wildcard):
    wildcard = unicode(wildcard)
    return wildcard.replace(' ','')

def valid(wildcard):
    wildcard = _clean(wildcard)
    if wildcard not in wildcards:
        return False
    return True

def clean(wildcard):
    if not valid(wildcard):
        raise ValueError('\'{0}\' is not a valid IPv4 wildcard mask'.format(wildcard))
    wildcard = _clean(wildcard)
    return wildcard
