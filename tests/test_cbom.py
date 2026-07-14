"""
Unit tests for the CBOM generator.
"""

import unittest

from scanners.cbom.generate_cbom import GenerateCBOM


class TestCBOM(unittest.TestCase):

    def setUp(self):

        self.generator = GenerateCBOM()

    def test_generator_created(self):

        self.assertIsNotNone(self.generator)

    def test_run_method_exists(self):

        self.assertTrue(

            callable(getattr(self.generator, "run", None))

        )


if __name__ == "__main__":

    unittest.main()
