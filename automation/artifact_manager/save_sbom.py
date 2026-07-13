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

        destination = self.storage / project_name

        destination.mkdir(parents=True, exist_ok=True)

        shutil.copy2(source_file, destination)

        print(f"SBOM saved -> {destination}")
