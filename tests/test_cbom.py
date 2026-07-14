"""
Unit tests for the CBOM generator.
"""

import unittest
from pathlib import Path

from scanners.cbom.generate_cbom import CBOMGenerator


class TestCBOM(unittest.TestCase):

    def setUp(self):

        self.generator = CBOMGenerator()

    def test_generator_created(self):

        self.assertIsNotNone(self.generator)

    def test_output_directory_exists(self):

        output_path = Path("output/cbom")

        output_path.mkdir(parents=True, exist_ok=True)

        self.assertTrue(output_path.exists())

        self.assertTrue(output_path.is_dir())


if __name__ == "__main__":

    unittest.main()
