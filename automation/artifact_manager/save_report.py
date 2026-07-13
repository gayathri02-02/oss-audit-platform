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

        from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

history = self.storage / project_name / today
latest = self.storage / project_name / "latest"

history.mkdir(parents=True, exist_ok=True)
latest.mkdir(parents=True, exist_ok=True)

filename = Path(source_file).name

shutil.copy2(source_file, history / filename)
shutil.copy2(source_file, latest / filename)

        print(f"Report saved -> {destination}")
