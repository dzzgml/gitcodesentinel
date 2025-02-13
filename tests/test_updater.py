import unittest
from core.updater import Updater

class TestUpdater(unittest.TestCase):
    def test_fetch_updates(self):
        updater = Updater()
        result = updater.fetch_updates('repo1')
        self.assertIsNone(result)

    def test_check_for_new_activity(self):
        updater = Updater()
        updater.check_for_new_activity(['repo1', 'repo2'])
