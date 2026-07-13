"""
validate_scanoss.py

Validate SCANOSS output.
"""

from pathlib import Path


class ScanOSSValidator:

    REQUIRED = [

        "packages"

    ]

    def validate(self, file_path):

        if not Path(file_path).exists():
            return False

        return True
