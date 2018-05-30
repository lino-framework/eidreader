from atelier.test import TestCase
from eidreader.setup_info import SETUP_INFO

class PackagesTest(TestCase):
    def test_packages(self):
        self.run_packages_test(SETUP_INFO['packages'])


