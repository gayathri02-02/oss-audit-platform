"""
Unit tests for the AI Report Generator.
"""

import unittest

from ai.report_generator.generate_report import ReportGenerator


class TestReports(unittest.TestCase):

    def setUp(self):

        self.generator = ReportGenerator()

    def test_report_generator_created(self):

        self.assertIsNotNone(self.generator)

    def test_generate_method_exists(self):

        self.assertTrue(

            callable(getattr(self.generator, "generate", None))

        )

    def test_required_components_exist(self):

        self.assertIsNotNone(self.generator.summary)

        self.assertIsNotNone(self.generator.score)

        self.assertIsNotNone(self.generator.crypto)

        self.assertIsNotNone(self.generator.recommendation)

        self.assertIsNotNone(self.generator.pdf)


if __name__ == "__main__":

    unittest.main()
