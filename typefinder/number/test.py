# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_true, assert_false, assert_raises

import integer
import floating

class Test_integer(object):
    """ Test integer """

    def test_validion(self):
        assert_true(integer.valid(650.0))
        assert_true(integer.valid(650))
        assert_true(integer.valid("650"))
        assert_true(integer.valid(u"650"))
        assert_false(integer.valid(650.2))
        assert_false(integer.valid('.2'))

    def test_cleaning(self):
        assert_equals(integer.clean('222'), 222)
        assert_equals(integer.clean(' 222 '), 222)
        assert_equals(integer.clean('1.0'), 1)
        assert_raises(ValueError, integer.clean, 'crap')

    def test_search(self):
        assert_equals(integer.search('this is integer 222'), [222])

class Test_floating(object):
    """ Test floating """

    def test_validion(self):
        for num in range(1,256):
            assert_true(floating.valid('.{0}'.format(num)))
        assert_true(floating.valid(1.1))
        assert_true(floating.valid('1.1'))
        assert_true(floating.valid(u'1.1'))
        assert_true(floating.valid(u'.1'))
        assert_false(floating.valid(650))
        assert_false(floating.valid('650'))

    def test_cleaning(self):
        assert_equals(floating.clean('1.2'), 1.2)
        assert_equals(floating.clean(' 1.2 '), 1.2)
        assert_raises(ValueError, floating.clean, 'crap')

    def test_search(self):
        assert_equals(floating.search('this is float 1.2'), [1.2])
        assert_equals(floating.search('this is float .2'), [.2])
