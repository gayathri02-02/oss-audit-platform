"""
cleanup_repo.py

Remove cloned repositories after pipeline execution.
"""

import shutil
import os


class CleanupRepository:

    def __init__(self):
        self.workspace = "workspace"

    def cleanup(self):

        if os.path.exists(self.workspace):

            print("Removing workspace...")

            shutil.rmtree(self.workspace)

            print("Workspace removed.")
