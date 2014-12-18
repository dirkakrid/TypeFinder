# -*- coding: utf-8 -*-

import re

import date
import vlan
import ipv4
import generic

from configuration import Configuration

_checks = 2
_passed_checks = 0

what = 'hostname'

def search(text):
    text = generic.clean(text)
    text = ' '.join([x.lower().strip('.,') for x in text.split()])
    for t in (ipv4.ip, ipv4.network, ipv4.ip_range, ipv4.subnet, ipv4.wildcard, vlan):
        text = generic.remove_type(text, t)
    hostnames = list()
    for token in text.split():
        if valid(token):
            token = clean(token)
            hostnames.append(token)
    return hostnames

def _using_dns_root_zone(hostname):
    labels = hostname.split('.')
    if len(labels) == 1:
        return False
    return labels[-1] in Configuration.dns_root_zones

def _read_host_file():
    if Configuration.host_file and not Configuration.known_hosts:
        try:
            with open(Configuration.host_file, 'r') as f:
                Configuration.known_hosts = f.readlines()
            Configuration.known_hosts = [_clean(host) for host in Configuration.known_hosts]
            Configuration.known_hosts = Configuration.known_hosts + [host.split('.')[0] for host in Configuration.known_hosts]
            Configuration.known_hosts = set(Configuration.known_hosts)
        except IOError:
            pass
    return Configuration.known_hosts

def _in_host_file(hostname):
    hosts = _read_host_file()
    if hostname in hosts:
        return True
    if hostname.split('.')[0] in hosts:
        return True
    return False

def _host_length(hostname):
    if len(hostname) > 253:
        #print(u"'{0}' too long".format(hostname))
        return False
    for label in hostname.split('.'):
        # http://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_host_names
        if len(label) < 0:
            #print(u"'{0}' too short".format(label))
            return False
        if len(label) > 63:
            #print(u"'{0}' too long".format(label))
            return False
    return True

def _host_characters(hostname):
    if re.match(Configuration.rfc1123_hostname, hostname, re.I):
        for label in hostname.split('.'):
            if not re.match(Configuration.rfc1123_hostname_label, label, re.I):
                #print(u"'{0}' label not RFC1123 compliant".format(label))
                return False
        return True
    #print(u"'{0}' hostname not RFC1123 compliant".format(hostname))
    return False

def _host_ends_with_number(hostname):
    if re.search(r'[a-z]+\d+$', hostname.split('.')[0], re.I):
        return True
    return False

def _host_starts_with_country_code(hostname):
    return len(hostname) > 1 and hostname[:2] in Configuration.country.keys()
    
def _dotted_notation(hostname):
    if hostname.count('.'):
        # Verify this is not an IP address
        return not ipv4.ip.valid(hostname) and not ipv4.ip_range.valid(hostname)
    return False

def _host_pattern(hostname):
    """ Commonly used words & patterns in hostnames """
    for hostname_pattern in Configuration.hostname_re:
        if re.search(hostname_pattern, hostname, re.I):
            return True
    return False

def _clean(hostname):
    hostname = hostname.decode('utf-8')
    hostname = hostname.strip(' ,.:#').lower().replace('\n', '').replace('\r', '')
    return hostname

def valid(hostname):
    _passed_checks = 0
    hostname = _clean(hostname)
    confidence = 0
    # Invalid Hostname checks
    if not _host_length(hostname) or not _host_characters(hostname):
        return False
    if date.valid(hostname):
        return False
    if vlan.valid(hostname):
        return False
    if _in_host_file(hostname):
        #print(u'{0} valid 1'.format(hostname))
        _passed_checks += 1
        confidence = 1
        return True
    if _using_dns_root_zone(hostname):
        #print(u'{0} valid 2'.format(hostname))
        _passed_checks += 1
        confidence += .50
    if _host_starts_with_country_code(hostname):
        #print(u'{0} valid 3'.format(hostname))
        _passed_checks += 1
        confidence += .15
    if _host_ends_with_number(hostname):
        #print(u'{0} valid 4'.format(hostname))
        _passed_checks += 1
        confidence += .35
    if _dotted_notation(hostname):
        #print(u'{0} valid 5'.format(hostname))
        _passed_checks += 1
        confidence += .50
    if _host_pattern(hostname):
        #print(u'{0} valid 6'.format(hostname))
        _passed_checks += 1
        confidence += .50
    if confidence >= .50:
        return True
    return False

def clean(hostname):
    if valid(hostname):
        return _clean(hostname)
    raise ValueError('\'{0}\' is not a valid hostname'.format(hostname))
