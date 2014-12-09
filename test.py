# -*- coding: utf-8 -*-

import time
import os
import datetime

from nose.tools import assert_equals, assert_true, assert_false, assert_raises

from ..configuration import Configuration

import plan.types.vlan as vlan
import plan.types.date as date
import plan.types.hostname as hostname

class Test_vlan(object):
    """ Test vlan """

    def test_validion(self):
        for x in range(1, 4097):
            assert_true(vlan.valid(x))
            assert_true(vlan.valid(str(x)))
        assert_false(vlan.valid('05/07/2012'))

    def test_cleaning(self):
        assert_equals(vlan.clean('222'), 222)
        assert_raises(ValueError, vlan.clean, 'crap')

    def test_search(self):
        assert_equals(vlan.search('this is vlan 222'), [222])
        assert_equals(vlan.search('this is vlan id vlan-4096'), [4096])
        assert_equals(vlan.search('this is vlan id vlan-0'), [])
        assert_equals(vlan.search('this is vlan id 2'), [2])
        assert_equals(vlan.search('this is 3'), [3])
        assert_equals(vlan.search('.4'), [])
        assert_equals(vlan.search('10.0.0.128-10.0.0.191, 10.0.0.192-10.0.0.255'), [])
        assert_equals(vlan.search('Server01'), [])
        assert_equals(vlan.search('Server01prod'), [])
        assert_equals(vlan.search('05/07/2012'), [])

class Test_hostname(object):
    """ Test hostname """

    def setup(self):
        """ Create a dummy host file """
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S%f')
        self.file_name = '{0}.txt'.format(self.timestamp)
        host_entries = ['from-host-file', 'from-host-file-again']
        Configuration.host_file = self.file_name
        with open(self.file_name, 'w+') as f:
            for host in host_entries:
                f.write(u'{0}\n'.format(host))

    def teardown(self):
        """ Create a dummy host file """
        os.remove(self.file_name)

    def test_validion_rfc(self):
        # Max label length
        assert_true(hostname.valid('dk' + 'x' * 59 + '01'))
        assert_false(hostname.valid('dk' + 'x' * 60 + '01'))
        assert_false(hostname.valid('x..x'))

        # Max hostname length
        assert_false(hostname.valid(''))
        assert_true(hostname.valid(('dk' + 'x' * 59 + '01.') * 3 + ('dk' + 'x' * 57 + '01.')))
        assert_false(hostname.valid(('dk' + 'x' * 59 + '01.') * 3 + ('dk' + 'x' * 58 + '01.')))

        # Valid Character Set
        assert_true(hostname.valid('01server.domain.root'))
        # Invalid Character Set
        assert_false(hostname.valid('-server'))
        assert_false(hostname.valid('server.-domain.root'))
        assert_false(hostname.valid('-server.domain.root'))
        assert_false(hostname.valid('øserver'))

    def test_validion(self):

        assert_true(hostname.valid('server.domain.root'))
        assert_true(hostname.valid('dkserver01'))
        assert_true(hostname.valid('srva'))
        assert_true(hostname.valid('srvb'))
        assert_true(hostname.valid('sqla'))
        assert_true(hostname.valid('sqlb'))
        assert_true(hostname.valid('appa'))
        assert_true(hostname.valid('appb'))
        assert_false(hostname.valid('05/07/2012'))

        # Bug fix: matching only the root level domain
        assert_false(hostname.valid('com'))

        # Host file matches
        assert_true(hostname.valid('from-host-file'))
        assert_true(hostname.valid('from-host-file-again'))

        assert_false(hostname.valid('dkserver'))
        assert_false(hostname.valid('1.1.1.1'))
        assert_false(hostname.valid('10.0.9.0-10.0.9.63'))
        assert_false(hostname.valid('12'))
        assert_false(hostname.valid('dksrv_01'))

        # Too ambiguous
        assert_false(hostname.valid('server'))
        
    def test_cleaning(self):
        assert_equals(hostname.clean('.,:HOST.SERVER.DOMAIN.,:'), 'host.server.domain')

    def test_search(self):
        assert_equals(hostname.search('blah blah server.host.domain, blah blah'), ['server.host.domain'])
        assert_equals(hostname.search('blah blah server.host.domain:'), ['server.host.domain'])
        assert_equals(hostname.search('server.host.domain blah blah'), ['server.host.domain'])
        assert_equals(hostname.search('blah blah  255.255.255.192'), [])
        assert_equals(hostname.search('blah blah 0.0.0.255'), [])
        assert_equals(hostname.search('blah blah 1.2.3.4 255.255.255.0'), [])
        assert_equals(hostname.search('blah blah 1.2.3.4-2.3.4.5'), [])

class Test_date(object):
    """ Test date """

    def test_validion(self):
        assert_true(date.valid('20-01-2014'))
        assert_true(date.valid('20 01 2014'))
        assert_true(date.valid('20/01/2014'))
        assert_true(date.valid('20.01.2014'))
        
    def test_cleaning(self):
        assert_equals(date.clean('20/01/2014'), '20-01-2014')
        assert_equals(date.clean('20 01 2014'), '20-01-2014')
        assert_equals(date.clean('20-01-2014'), '20-01-2014')
        assert_equals(date.clean('20.01.2014'), '20-01-2014')
        assert_raises(ValueError, date.clean, 'crap')

    def test_search(self):
        assert_equals(date.search('blah blah 20 01 2014 blah blah'), ['20-01-2014'])
        assert_equals(date.search('20-01-2014 blah blah'), ['20-01-2014'])
        assert_equals(date.search('blah blah 20/01/2014'), ['20-01-2014'])
        assert_equals(date.search('23-06-2008'), ['23-06-2008'])
        
