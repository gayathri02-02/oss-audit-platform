"""
save_report.py

Save generated AI reports into the storage directory.
"""

import shutil
from pathlib import Path


class SaveReport:

    def __init__(self):
        self.storage = Path("storage/reports")

    def save(self, project_name, source_file):

        destination = self.storage / project_name

        destination.mkdir(parents=True, exist_ok=True)

        shutil.copy2(source_file, destination)

        print(f"Report saved -> {destination}")
