# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_not_equals, assert_true, assert_false, assert_raises

import ip, network, ip_range, wildcard, subnet

class Test_ip_range(object):
    """ Test ip_range """

    def test_validion(self):
        assert_true(ip_range.valid('1.1.1.1-1.1.1.2'))
        assert_true(ip_range.valid(' 1.1.1.1 - 1.1.1.2   '))
        assert_false(ip_range.valid(' 1.1.1.1 - 1.1.1.a   '))
        assert_false(ip_range.valid('1.1.1.1'))
        assert_false(ip_range.valid('1.1.1.0/24'))
        
    def test_cleaning(self):
        assert_equals(ip_range.clean(' 1.1.1.2 - 1.1.1.1   '), '1.1.1.1-1.1.1.2')
        assert_raises(ValueError, ip_range.clean, '1.1.1.0/24')

    def test_search(self):
        assert_equals(ip_range.search('blah blah 1.1.1.2 - 1.1.1.1   '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ip_range.search(' 1.1.1.2 - 1.1.1.1  blah blah '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ip_range.search('blah blah 1.1.1.2 - 1.1.1.1  blah blah '), ['1.1.1.1-1.1.1.2'])
        assert_equals(ip_range.search('Server net 10.0.0.0-10.0.0.63, 10.0.0.64-10.0.0.127, 10.0.0.128-10.0.0.191, 10.0.0.192-10.0.0.255'), ['10.0.0.0-10.0.0.63', '10.0.0.64-10.0.0.127', '10.0.0.128-10.0.0.191', '10.0.0.192-10.0.0.255'])

    def test_get_network(self):
        assert_equals(ip_range.get_network('1.1.1.1-1.1.1.2'), '1.1.1.0/30')
        assert_equals(ip_range.get_network('0.0.0.0-255.255.255.255'), '0.0.0.0/0')
        assert_equals(ip_range.get_network('1.1.1.1-1.1.1.1'), '1.1.1.1/32')

class Test_ip(object):
    """ Test ip """

    def test_validion(self):
        assert_true(ip.valid('1.1.1.1'))
        assert_false(ip.valid('1.1.1.1/24'))
        assert_false(ip.valid('1.1.1.1-1.1.1.2'))
        # Allow subnets to match subnet ips
        for _subnet in subnet.subnets:
            assert_false(ip.valid(_subnet))

        
    def test_cleaning(self):
        assert_equals(ip.clean('1.1.1.1'), '1.1.1.1')
        assert_raises(ValueError, ip.clean, '1.1.1.0/24')

    def test_search(self):
        assert_equals(ip.search('blah blah 1.2.3.4, blah blah'), ['1.2.3.4'])
        assert_equals(ip.search('blah blah 1.2.3.4 255.255.255.255 blah blah'), [])
        assert_equals(ip.search('blah blah 1.2.3.4 255.255.255.255'), [])
        assert_equals(ip.search('1.2.3.4 255.255.255.255 blah blah '), [])
        assert_equals(ip.search('1.2.3.4 blah blah '), ['1.2.3.4'])
        assert_equals(ip.search('1.2.3.4 2.3.4.5 blah blah '), ['1.2.3.4', '2.3.4.5'])
        assert_equals(ip.search('blah blah 1.2.3.4 2.3.4.5  '), ['1.2.3.4', '2.3.4.5'])
        assert_equals(ip.search('blah blah 1.2.3.4-2.3.4.5  '), [])
        assert_equals(ip.search('blah 1.2.3.4-2.3.4.5 blah  '), [])
        assert_equals(ip.search('1.2.3.4-2.3.4.5 blah blah  '), [])
        assert_equals(ip.search('1.2.3.4 - 2.3.4.5 blah blah  '), [])
        assert_equals(ip.search('1.2.3.4/255.2555.255.0 blah blah  '), [])
        assert_equals(ip.search('1.2.3.4 / 255.2555.255.0 blah blah  '), [])
        assert_equals(ip.search('10.0.0.128-10.0.0.191, 10.0.0.192-10.0.0.255'), [])

class Test_network(object):
    """ Test network """

    def test_validion(self):
        assert_true(network.valid('1.1.1.1/24'))
        assert_false(network.valid('1.1.1.1'))
        assert_false(network.valid('1.1.1.1-1.1.1.2'))
        assert_false(network.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(network.clean('1.1.1.1/24'), '1.1.1.0/24')
        assert_raises(ValueError, network.clean, '1.1.1.1')

    def test_special(self):
        """ Non standard """
        assert_equals(network.clean('1.1.1.1/24'), '1.1.1.0/24')
        assert_raises(ValueError, network.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(network.search('blah blah 1.2.3.4 255.255.255.0. blah'), ['1.2.3.0/24'])
        assert_equals(network.search('blah blah 1.2.3.4/255.255.255.0, blah'), ['1.2.3.0/24'])
        assert_equals(network.search('blah blah 1.2.0.0/16 blah'), ['1.2.0.0/16'])

class Test_subnet(object):
    """ Test subnet """

    def test_validion(self):
        assert_true(subnet.valid('255.255.255.255'))
        assert_true(subnet.valid('255.255.255.0'))
        assert_true(subnet.valid('255.255.192.0'))
        assert_true(subnet.valid('0.0.0.0'))
        assert_false(subnet.valid('1.1.1.1'))
        assert_false(subnet.valid('1.1.1.1-1.1.1.2'))
        assert_false(subnet.valid('0.0.0.255'))
        assert_false(subnet.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(subnet.clean(' 255.255.255.255 '), '255.255.255.255')
        assert_raises(ValueError, subnet.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(subnet.search('255.255.128.0'), ['255.255.128.0'])
        assert_equals(subnet.search('255.255.1.0'), [])
        assert_equals(subnet.search('blah blah 255.255.255.0. blah'), ['255.255.255.0'])
        assert_equals(subnet.search('blah blah 1.2.3.4 255.255.255.0. blah'), [])
        assert_equals(subnet.search('blah blah 1.2.3.4 / 255.255.255.0. blah'), [])
        assert_equals(subnet.search('blah blah 1.2.3.4 - 255.255.255.0. blah'), [])

class Test_wildcard(object):
    """ Test wildcard """

    def test_validion(self):
        assert_true(wildcard.valid('255.255.255.255'))
        assert_true(wildcard.valid('0.0.0.0'))
        assert_true(wildcard.valid('0.0.0.255'))
        assert_true(wildcard.valid('0.3.255.255'))
        assert_false(wildcard.valid('255.255.255.0'))
        assert_false(wildcard.valid('255.255.192.0'))
        assert_false(wildcard.valid('1.1.1.1'))
        assert_false(wildcard.valid('1.1.1.1-1.1.1.2'))
        assert_false(wildcard.valid('crap'))
        
    def test_cleaning(self):
        assert_equals(wildcard.clean(' 0.0.127.255 '), '0.0.127.255')
        assert_raises(ValueError, wildcard.clean, '1.1.1.1')

    def test_search(self):
        assert_equals(wildcard.search('0.0.0.255'), ['0.0.0.255'])
        assert_equals(wildcard.search('0.0.0.211'), [])
        assert_equals(wildcard.search('blah blah 0.0.255.255. blah'), ['0.0.255.255'])
        assert_equals(wildcard.search('blah blah 1.2.3.4 0.0.255.255. blah'), [])
        assert_equals(wildcard.search('blah blah 1.2.3.4 / 0.255.255.255. blah'), [])
        assert_equals(wildcard.search('blah blah 1.2.3.4 - 0.255.255.255. blah'), [])

