# -*- coding: utf-8 -*-
import re

import date
import ipv4

import number
import generic

vlan_id_re = r'(?<![\-\.\da-z])(?:vlan[- ]?(?:\s+id\s+)?)?\d+(?![\.\d\-a-z])'

def _remove_invalid_types(text):
    text = generic.remove_type(text, date)
    text = generic.remove_type(text, ipv4.ip)
    text = generic.remove_type(text, ipv4.network)
    text = generic.remove_type(text, ipv4.ip_range)
    return text

def search(text):
    text = ' '.join(unicode(text).split()).strip(',')
    vlans = list()
    text = _remove_invalid_types(text)
    matches = re.findall(vlan_id_re, text, re.I)
    for match in matches:
        match = match.lower().replace('vlan','').replace('-', '')
        match = match.replace('id', '')
        match = match.strip()
        if valid(match):
            vlans.append(clean(match))
    for match in text.split():
        if valid(match):
            vlan_id = clean(match)
            if vlan_id not in vlans:
                vlans.append(vlan_id)
    return vlans

def valid(vlan_id):
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
