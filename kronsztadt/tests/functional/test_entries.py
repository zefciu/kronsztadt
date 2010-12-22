from kronsztadt.tests import *

class TestEntriesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='entries', action='index'))
        # Test response...
