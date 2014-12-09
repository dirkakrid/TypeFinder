# -*- coding: utf-8 -*-
import re
import ipaddress

from .. import generic


def supernets(network):
    """ Return supernets of the network """
    network = clean(network)
    network = ipaddress.IPv4Network(network)
    current_prefix = network.prefixlen
    supernets = list()
    for prefix in reversed(range(0, current_prefix + 1)):
        supernets.append(network.supernet(new_prefix=prefix).exploded)
    return supernets[1:]

def subnets(network):
    """ Return subnets of the network """
    network = clean(network)
    network = ipaddress.IPv4Network(network)
    current_prefix = network.prefixlen
    subnets = list()
    if current_prefix == 32:
        subnets.append(network.exploded)
    else:
        for prefix in range(current_prefix, 32):
            for current_network in network.subnets(new_prefix=prefix):
                subnets.append(current_network.exploded)
    return subnets

def string_prefix(network):
    """ 
        Returns the common string prefix of a network and all it's hosts 
    """
    network = clean(network)
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
