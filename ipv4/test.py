# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_not_equals, assert_true, assert_false, assert_raises

import plan.types.ipv4 as ipv4

class Test_ip_range(object):
    """ Test ip_range """

    def test_validion(self):
        assert_true(ipv4.ip_range.valid('1.1.1.1-1.1.1.2'))
        assert_true(ipv4.ip_range.valid(' 1.1.1.1 - 1.1.1.2   '))
        assert_false(ipv4.ip_range.valid(' 1.1.1.1 - 1.1.1.a   '))
        assert_false(ipv4.ip_range.valid('1.1.1.1'))
        assert_false(ipv4.ip_range.valid('1.1.1.0/24'))
        
    def test_cleaning(self):
        assert_equals(ipv4.ip_range.clean(' 1.1.1.2 - 1.1.1.1   '), '1.1.1.1-1.1.1.2')
        assert_raises(ValueError, ipv4.ip_range.clean, '1.1.1.0/24')

    def test_search(self):
        assert_equals(ipv4.ip_range.search('blah blah 1.1.1.2 - 1.1.1.1   '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ipv4.ip_range.search(' 1.1.1.2 - 1.1.1.1  blah blah '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ipv4.ip_range.search('blah blah 1.1.1.2 - 1.1.1.1  blah blah '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ipv4.ip_range.search('Server net 10.0.0.0-10.0.0.63, 10.0.0.64-10.0.0.127, 10.0.0.128-10.0.0.191, 10.0.0.192-10.0.0.255'), ['10.0.0.0-10.0.0.63', '10.0.0.64-10.0.0.127', '10.0.0.128-10.0.0.191', '10.0.0.192-10.0.0.255'])

    def test_get_network(self):
        assert_equals(ipv4.ip_range.get_network('1.1.1.1-1.1.1.2'), '1.1.1.0/30')
        assert_equals(ipv4.ip_range.get_network('0.0.0.0-255.255.255.255'), '0.0.0.0/0')
        assert_equals(ipv4.ip_range.get_network('1.1.1.1-1.1.1.1'), '1.1.1.1/32')

class Test_ip(object):
    """ Test ip """

    def test_validion(self):
        assert_true(ipv4.ip.valid('1.1.1.1'))
        assert_false(ipv4.ip.valid('1.1.1.1/24'))
        assert_false(ipv4.ip.valid('1.1.1.1-1.1.1.2'))
        # Allow subnets to match subnet ips
        for _subnet in ipv4.subnet.subnets:
            assert_false(ipv4.ip.valid(_subnet))

        
    def test_cleaning(self):
        assert_equals(ipv4.ip.clean('1.1.1.1'), '1.1.1.1')
        assert_raises(ValueError, ipv4.ip.clean, '1.1.1.0/24')

    def test_search(self):
        assert_equals(ipv4.ip.search('blah blah 1.2.3.4, blah blah'), ['1.2.3.4'])
        assert_equals(ipv4.ip.search('blah blah 1.2.3.4 255.255.255.255 blah blah'), [])
        assert_equals(ipv4.ip.search('blah blah 1.2.3.4 255.255.255.255'), [])
        assert_equals(ipv4.ip.search('1.2.3.4 255.255.255.255 blah blah '), [])
        assert_equals(ipv4.ip.search('1.2.3.4 blah blah '), ['1.2.3.4'])
        assert_equals(ipv4.ip.search('1.2.3.4 2.3.4.5 blah blah '), ['1.2.3.4', '2.3.4.5'])
        assert_equals(ipv4.ip.search('blah blah 1.2.3.4 2.3.4.5  '), ['1.2.3.4', '2.3.4.5'])
        assert_equals(ipv4.ip.search('blah blah 1.2.3.4-2.3.4.5  '), [])
        assert_equals(ipv4.ip.search('blah 1.2.3.4-2.3.4.5 blah  '), [])
        assert_equals(ipv4.ip.search('1.2.3.4-2.3.4.5 blah blah  '), [])
        assert_equals(ipv4.ip.search('1.2.3.4 - 2.3.4.5 blah blah  '), [])
        assert_equals(ipv4.ip.search('1.2.3.4/255.2555.255.0 blah blah  '), [])
        assert_equals(ipv4.ip.search('1.2.3.4 / 255.2555.255.0 blah blah  '), [])
        assert_equals(ipv4.ip.search('10.0.0.128-10.0.0.191, 10.0.0.192-10.0.0.255'), [])

class Test_network(object):
    """ Test network """

    def test_validion(self):
        assert_true(ipv4.network.valid('1.1.1.1/24'))
        assert_false(ipv4.network.valid('1.1.1.1'))
        assert_false(ipv4.network.valid('1.1.1.1-1.1.1.2'))
        assert_false(ipv4.network.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(ipv4.network.clean('1.1.1.1/24'), '1.1.1.0/24')
        assert_raises(ValueError, ipv4.network.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(ipv4.network.search('blah blah 1.2.3.4 255.255.255.0. blah'), ['1.2.3.0/24'])
        assert_equals(ipv4.network.search('blah blah 1.2.3.4/255.255.255.0, blah'), ['1.2.3.0/24'])
        assert_equals(ipv4.network.search('blah blah 1.2.0.0/16 blah'), ['1.2.0.0/16'])

class Test_subnet(object):
    """ Test subnet """

    def test_validion(self):
        assert_true(ipv4.subnet.valid('255.255.255.255'))
        assert_true(ipv4.subnet.valid('255.255.255.0'))
        assert_true(ipv4.subnet.valid('255.255.192.0'))
        assert_true(ipv4.subnet.valid('0.0.0.0'))
        assert_false(ipv4.subnet.valid('1.1.1.1'))
        assert_false(ipv4.subnet.valid('1.1.1.1-1.1.1.2'))
        assert_false(ipv4.subnet.valid('0.0.0.255'))
        assert_false(ipv4.subnet.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(ipv4.subnet.clean(' 255.255.255.255 '), '255.255.255.255')
        assert_raises(ValueError, ipv4.subnet.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(ipv4.subnet.search('255.255.128.0'), ['255.255.128.0'])
        assert_equals(ipv4.subnet.search('255.255.1.0'), [])
        assert_equals(ipv4.subnet.search('blah blah 255.255.255.0. blah'), ['255.255.255.0'])
        assert_equals(ipv4.subnet.search('blah blah 1.2.3.4 255.255.255.0. blah'), [])
        assert_equals(ipv4.subnet.search('blah blah 1.2.3.4 / 255.255.255.0. blah'), [])
        assert_equals(ipv4.subnet.search('blah blah 1.2.3.4 - 255.255.255.0. blah'), [])

class Test_wildcard(object):
    """ Test wildcard """

    def test_validion(self):
        assert_true(ipv4.wildcard.valid('255.255.255.255'))
        assert_true(ipv4.wildcard.valid('0.0.0.0'))
        assert_true(ipv4.wildcard.valid('0.0.0.255'))
        assert_true(ipv4.wildcard.valid('0.3.255.255'))
        assert_false(ipv4.wildcard.valid('255.255.255.0'))
        assert_false(ipv4.wildcard.valid('255.255.192.0'))
        assert_false(ipv4.wildcard.valid('1.1.1.1'))
        assert_false(ipv4.wildcard.valid('1.1.1.1-1.1.1.2'))
        assert_false(ipv4.wildcard.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(ipv4.wildcard.clean(' 0.0.127.255 '), '0.0.127.255')
        assert_raises(ValueError, ipv4.wildcard.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(ipv4.wildcard.search('0.0.0.255'), ['0.0.0.255'])
        assert_equals(ipv4.wildcard.search('0.0.0.211'), [])
        assert_equals(ipv4.wildcard.search('blah blah 0.0.255.255. blah'), ['0.0.255.255'])
        assert_equals(ipv4.wildcard.search('blah blah 1.2.3.4 0.0.255.255. blah'), [])
        assert_equals(ipv4.wildcard.search('blah blah 1.2.3.4 / 0.255.255.255. blah'), [])
        assert_equals(ipv4.wildcard.search('blah blah 1.2.3.4 - 0.255.255.255. blah'), [])

