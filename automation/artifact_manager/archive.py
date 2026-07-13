"""
archive.py

Archive old artifacts.
"""

import shutil
from pathlib import Path
from datetime import datetime


class Archive:

    def __init__(self):

        self.archive = Path("storage/archive")

    def archive_project(self, project_name):

        project_folder = Path("storage") / project_name

        if not project_folder.exists():
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        destination = self.archive / f"{project_name}_{timestamp}"

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.move(project_folder, destination)

        print(f"Archived {project_name}")
