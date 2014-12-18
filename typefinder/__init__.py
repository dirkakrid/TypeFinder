# -*- coding: utf-8 -*-
import ipv4
import ipv6
import date
import vlan
import hostname
import number

all_types = (ipv4.ip, ipv4.network, ipv4.subnet, ipv4.wildcard, ipv4.ip_range, hostname, vlan, date, number.integer, number.floating)
