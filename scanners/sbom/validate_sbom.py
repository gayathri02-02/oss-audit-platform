"""
validate_sbom.py
"""

from pathlib import Path


class SBOMValidator:

    def validate(self, file):

        return Path(file).exists()
