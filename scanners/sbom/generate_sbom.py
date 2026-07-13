"""
generate_sbom.py

Generate final SBOM.
"""

from scanners.scanoss.scanoss_runner import ScanOSSRunner
from scanners.scanoss.validate_scanoss import ScanOSSValidator


class GenerateSBOM:

    def run(self, project_name, repository):

        runner = ScanOSSRunner()

        validator = ScanOSSValidator()

        sbom = runner.scan(project_name, repository)

        if validator.validate(sbom):

            return sbom

        raise Exception("Invalid SBOM")
