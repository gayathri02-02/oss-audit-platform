"""
generate_cbom.py
"""

from scanners.cryptofinder.cryptofinder_runner import CryptoFinderRunner
from scanners.cryptofinder.validate_cbom import CBOMValidator


class GenerateCBOM:

    def run(self, project_name, repository):

        runner = CryptoFinderRunner()

        validator = CBOMValidator()

        cbom = runner.scan(project_name, repository)

        if validator.validate(cbom):

            return cbom

        raise Exception("Invalid CBOM")
