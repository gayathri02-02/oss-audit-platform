"""
metadata.py

Maintain metadata for generated artifacts.
"""

import json
from pathlib import Path
from datetime import datetime


class Metadata:

    def __init__(self):

        self.metadata = Path("storage/metadata")

        self.metadata.mkdir(parents=True, exist_ok=True)

    def create(self,
               project_name,
               sbom,
               cbom,
               report,
               status):

        today = datetime.now().strftime("%Y-%m-%d")
                   data = {
                       "project": project_name,
                       "status": status,
                       "generated_on": datetime.now().isoformat(),
                       "scan_date": today,
                       "sbom": sbom,
                       "cbom": cbom,
                       "report": report
                       }
        output = self.metadata / f"{project_name}.json"

        with open(output, "w") as file:

            json.dump(data, file, indent=4)

        print(f"Metadata created -> {output}")
