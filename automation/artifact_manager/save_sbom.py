"""
save_sbom.py

Save generated SBOM files into the storage directory.
"""

import shutil
from pathlib import Path


class SaveSBOM:

    def __init__(self):
        self.storage = Path("storage/sboms")

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

        print(f"SBOM saved -> {destination}")
