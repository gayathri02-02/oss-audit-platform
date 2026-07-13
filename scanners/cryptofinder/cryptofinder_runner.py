"""
cryptofinder_runner.py

Runs CryptoFinder.
"""

import subprocess
from pathlib import Path


class CryptoFinderRunner:

    def __init__(self):

        self.output = Path("output/cbom")

        self.output.mkdir(parents=True, exist_ok=True)

    def scan(self, project_name, repository):

        output = self.output / f"{project_name}_cbom.json"

        command = [

            "crypto-finder",

            "scan",

            repository,

            "--format",

            "cyclonedx",

            "--output",

            str(output)

        ]

        print("Running CryptoFinder...")

        subprocess.run(command, check=True)

        return output
