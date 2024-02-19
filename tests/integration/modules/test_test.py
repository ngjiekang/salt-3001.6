# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import logging

import pytest
import salt.config
import salt.version
from tests.support.case import ModuleCase
from tests.support.helpers import slowTest
from tests.support.mixins import AdaptedConfigurationTestCaseMixin

log = logging.getLogger(__name__)


@pytest.mark.windows_whitelisted
class TestModuleTest(ModuleCase, AdaptedConfigurationTestCaseMixin):
    """
    Validate the test module
    """

    @slowTest
    def test_ping(self):
        """
        test.ping
        """
        self.assertTrue(self.run_function("test.ping"))

    @slowTest
    def test_echo(self):
        """
        test.echo
        """
        self.assertEqual(self.run_function("test.echo", ["text"]), "text")

    @slowTest
    def test_version(self):
        """
        test.version
        """
        self.assertEqual(
            self.run_function("test.version"), salt.version.__saltstack_version__.string
        )

    @slowTest
    def test_conf_test(self):
        """
        test.conf_test
        """
        self.assertEqual(self.run_function("test.conf_test"), "baz")

    @slowTest
    def test_get_opts(self):
        """
        test.get_opts
        """
        opts = salt.config.minion_config(self.get_config_file_path("minion"))
        self.assertEqual(
            self.run_function("test.get_opts")["cachedir"], opts["cachedir"]
        )

    @slowTest
    def test_cross_test(self):
        """
        test.cross_test
        """
        self.assertTrue(self.run_function("test.cross_test", ["test.ping"]))

    @slowTest
    def test_fib(self):
        """
        test.fib
        """
        self.assertEqual(self.run_function("test.fib", ["20"],)[0], 6765)

    @slowTest
    def test_collatz(self):
        """
        test.collatz
        """
        self.assertEqual(self.run_function("test.collatz", ["40"],)[0][-1], 2)

    @slowTest
    def test_outputter(self):
        """
        test.outputter
        """
        self.assertEqual(self.run_function("test.outputter", ["text"]), "text")