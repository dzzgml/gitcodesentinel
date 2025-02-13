import unittest
from core.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        report_generator = ReportGenerator()
        report_generator.generate_report(['update1', 'update2'], frequency='daily')

    def test_format_report(self):
        report_generator = ReportGenerator()
        report_generator.format_report(['update1', 'update2'])
