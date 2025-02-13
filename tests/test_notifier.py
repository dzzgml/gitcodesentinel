import unittest
from core.notifier import Notifier

class TestNotifier(unittest.TestCase):
    def test_send_email_notification(self):
        notifier = Notifier()
        notifier.send_email_notification('user1', 'Test content')

    def test_generate_summary_report(self):
        notifier = Notifier()
        notifier.generate_summary_report(['update1', 'update2'])
