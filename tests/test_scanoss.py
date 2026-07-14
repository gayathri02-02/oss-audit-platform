"""
Unit tests for the SCANOSS scanner.
"""

import unittest
from pathlib import Path

from scanners.scanoss.scanoss_runner import ScanOSSRunner


class TestScanOSS(unittest.TestCase):

    def setUp(self):

        self.runner = ScanOSSRunner()

    def test_output_directory_exists(self):

        self.assertTrue(self.runner.output.exists())

    def test_output_directory_is_directory(self):

        self.assertTrue(self.runner.output.is_dir())


if __name__ == "__main__":

    unittest.main()
