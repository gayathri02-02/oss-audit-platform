"""
Unit tests for the AI Report Generator.
"""

import unittest

from ai.report_generator.generate_report import ReportGenerator


class TestReports(unittest.TestCase):

    def setUp(self):

        self.report_generator = ReportGenerator()

    def test_report_generator_created(self):

        self.assertIsNotNone(self.report_generator)

    def test_generate_method_exists(self):

        self.assertTrue(

            callable(getattr(self.report_generator, "generate", None))

        )


if __name__ == "__main__":

    unittest.main()
