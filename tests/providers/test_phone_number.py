# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Factory
from .. import string_types


class TestJaJP(unittest.TestCase):
    """ Tests phone_number in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_phone_number(self):
        pn = self.factory.phone_number()
        formats = ('070', '080', '090')

        assert pn
        assert isinstance(pn, string_types)
        first, second, third = pn.split('-')
        assert first
        assert first.isdigit()
        assert second
        assert second.isdigit()
        assert third
        assert third.isdigit()
        if len(first) == 2:
            assert len(second) == 4
            assert len(third) == 4
        else:
            assert len(first) == 3
            assert len(second) == 4
            assert len(third) == 4
            assert first in formats



class TestMSISDN(unittest.TestCase):
    """ Tests MSISDN in the pt_br locale """

    def setUp(self):
        self.factory = Factory.create('pt_br')

    def test_msisdn(self):
        msisdn = self.factory.msisdn()
        formats = ('5511', '5521', '5531', '5541', '5551', '5561', '5571', '5581')

        assert msisdn is not None
        assert isinstance(msisdn, string_types)
        assert len(msisdn) == 13
        assert msisdn.isdigit()
        assert msisdn[0:4] in formats