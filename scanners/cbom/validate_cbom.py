"""
validate_cbom.py
"""

from pathlib import Path


class CBOMValidator:

    def validate(self, file):

        return Path(file).exists()
