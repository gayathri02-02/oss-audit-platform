"""
scanoss_runner.py

Runs SCANOSS to generate SBOM.
"""

import subprocess
from pathlib import Path


class ScanOSSRunner:

    def __init__(self):

        self.output = Path("output/scanoss")

        self.output.mkdir(parents=True, exist_ok=True)

    def scan(self, project_name, repository):

        output_file = self.output / f"{project_name}_scanoss.json"

        command = [

            "scanoss-py",

            "scan",

            repository,

            "--format",

            "cyclonedx",

            "--output",

            str(output_file)

        ]

        print("Running SCANOSS...")

        subprocess.run(command, check=True)

        return output_file
