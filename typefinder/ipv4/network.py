# -*- coding: utf-8 -*-
import re
import ipaddress

from .. import generic

def string_prefix(network):
    """ 
        Returns the common string prefix of a network and all it's hosts 
    """
    valid(network)
    network_prefix = u""
    network = ipaddress.IPv4Network(network)
    for index, place in enumerate(network.network_address.exploded):
        if place != network.broadcast_address.exploded[index]:
            break
        network_prefix += place
    network_prefix += "*"
    return network_prefix

def search(text):
    text = generic.clean(text)
    text = ' '.join(unicode(text).split())
    matches = re.findall('(?:\d+\.){3}\d+/\d+', text, re.I)
    matches = matches + re.findall('(?:\d+\.){3}\d+/(?:\d+\.){3}\d+', text, re.I)
    matches = matches + [_clean(x) for x in re.findall('(?:\d+\.){3}\d+\s+(?:\d+\.){3}\d+', text, re.I)]
    networks = list()
    for match in matches:
        if valid(match):
            networks.append(clean(match))
    return networks

def _clean(network):
    network = unicode(network)
    network = ' '.join(network.split())
    network = network.replace(' ', '/')
    return network

def valid(network):
    network = _clean(network)
    try:
        network = ipaddress.IPv4Network(network)
    except ipaddress.AddressValueError:
        return False
    except ipaddress.NetmaskValueError:
        return False
    except ValueError:
        network = ipaddress.IPv4Interface(network).network
    if network.prefixlen == 32:
        return False
    return True

def clean(network):
    if not valid(network):
        raise ValueError('\'{0}\' is not a valid IPv4 network'.format(network))
    network = _clean(network)
    return ipaddress.IPv4Interface(unicode(network)).network.exploded
