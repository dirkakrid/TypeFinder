# -*- coding: utf-8 -*-
import re

import date
import ipv4
import number
import generic

from configuration import Configuration

vlan_id_re = r'(?<![\-\.\da-z])(?:vlan[- ]?(?:\s+id\s+)?)?\d+(?![\.\d\-a-z])'

what = 'vlan'

def _remove_invalid_types(text):
    text = generic.remove_type(text, date)
    text = generic.remove_type(text, ipv4.ip)
    text = generic.remove_type(text, ipv4.network)
    text = generic.remove_type(text, ipv4.ip_range)
    return text

def _clean(vlan_id):
    vlan_id = ' '.join(unicode(vlan_id).split()).lower()
    for rep in ('vlan-id', 'vlan-', 'vlan'):
        vlan_id = vlan_id.replace(rep, '')
    vlan_id = vlan_id.strip()
    return vlan_id

def search(text):
    text = ' '.join(unicode(text).split()).strip(',')
    vlans = set()
    text = _remove_invalid_types(text)
    matches = list()
    for vlan_re in Configuration.valid_vlan_re:
        for match in re.findall(vlan_id_re, text, re.I):
            print 'match!:', match
            if valid(match):
                text = text.replace(match, '')
                vlans.add(_clean(match))

    for match in text.split():
        if valid(match):
            vlan_id = clean(match)
            if vlan_id not in vlans:
                vlans.add(vlan_id)
    return [clean(x) for x in vlans]

def valid(vlan_id):
    vlan_id = _clean(vlan_id)
    if number.integer.valid(vlan_id):
        if not date.valid(vlan_id):
            vlan_id = number.integer.clean(vlan_id)
            if vlan_id > 0 and vlan_id < 4097:
                return True
    return False

def clean(vlan_id):
    if valid(vlan_id):
        return number.integer.clean(vlan_id)
    raise ValueError('\'{0}\' is not a valid VLAN ID'.format(vlan_id))
