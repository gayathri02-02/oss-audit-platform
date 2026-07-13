"""
save_cbom.py

Save generated CBOM files into the storage directory.
"""

import shutil
from pathlib import Path


class SaveCBOM:

    def __init__(self):
        self.storage = Path("storage/cboms")

    def save(self, project_name, source_file):

        destination = self.storage / project_name

        destination.mkdir(parents=True, exist_ok=True)

        shutil.copy2(source_file, destination)

        print(f"CBOM saved -> {destination}")
