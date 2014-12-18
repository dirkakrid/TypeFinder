# -*- coding: utf-8 -*-
import re
import ipaddress
import subnet

from ..configuration import Configuration
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
    matches = list()
    for re_network_expresssion in Configuration.valid_ipv4_network_re:
        matches = matches + [_clean(x) for x in re.findall(re_network_expresssion, text, re.I)]
    networks = list()
    for match in matches:
        if valid(match):
            networks.append(clean(match))
    return networks

def fuzzy_search(text):
    """ Return fuzzy matches """
    exact_matches = search(text)
    text = generic.clean(text)
    text = ' '.join(unicode(text).split())
    matches = list()
    for re_network_expresssion in Configuration.fuzzy_ipv4_network_re:
        for match in re.findall(re_network_expresssion, text, re.I):
            # Remove matches from the text
            text = text.replace(match, '')
            text = ' '.join(text.split())
            matches.append(match)
    networks = list()
    for match in matches:
        if fuzzy_valid(match) and (match not in exact_matches):
            networks.append(clean(_fuzzy_clean(match)))
    return networks

def _fuzzy_clean(network):
    network = _clean(network)
    # 1.2.3.yyy -> 1.2.3.x
    network = re.sub(r'[a-zA-Z]{1,3}', 'x', network)
    if not re.search(r'/\d+$', network) and not subnet.valid(network.split('/')[-1]):
        classful_prefixes = (24, 16, 8)
        if network.count('x') in range(1, 4):
            network = '{0}/{1}'.format(network, classful_prefixes[network.count('x') - 1])
    network = network.replace('x', '0')
    return network

def _clean(network):
    network = unicode(network)
    network = ' '.join(network.split())
    network = network.replace(' ', '/')
    return network

def fuzzy_valid(network):
    invalid = True
    for re_network_expresssion in Configuration.fuzzy_ipv4_network_re:
        if re.findall(re_network_expresssion, network, re.I):
            invalid = False
            break
    if invalid:
        return False    
    network = _clean(network)
    network = _fuzzy_clean(network)
    for re_network_expresssion in Configuration.valid_ipv4_network_re:
        if re.findall(re_network_expresssion, network, re.I):
            return True
    return False

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
