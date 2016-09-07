from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite
import os

class CustomizedRunner(DiscoverRunner):
    def build_suite(self, *args, **kwargs):
        suite = super(CustomizedRunner, self).build_suite(*args, **kwargs)
        filtered = TestSuite()

        for test in suite:
            testname = str(test)
            if '.tests.' in testname and self.package in testname:
                filtered.addTest(test)
        return filtered


class UnitRunner(CustomizedRunner):
    package = '.unit.'

    def setup_databases(self, *args, **kwargs):
        pass

    def teardown_databases(self, *args, **kwargs):
        pass


class IntegrationRunner(CustomizedRunner):
    package = '.integration.'


class AcceptanceRunner(CustomizedRunner):
    package = '.acceptance.'
    os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8001'
