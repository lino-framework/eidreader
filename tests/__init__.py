from atelier.test import TestCase
from eidreader import SETUP_INFO

class PackagesTests(TestCase):
    def test_packages(self):
        self.run_packages_test(SETUP_INFO['packages'])


