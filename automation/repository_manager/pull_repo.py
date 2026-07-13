"""
pull_repo.py

Pull latest changes for cloned repositories.
"""

import os
import subprocess


class PullRepository:

    def __init__(self):
        self.workspace = "workspace"

    def pull_all(self):

        if not os.path.exists(self.workspace):
            return

        for project in os.listdir(self.workspace):

            repo_path = os.path.join(self.workspace, project)

            if not os.path.isdir(repo_path):
                continue

            print(f"Updating {project}")

            subprocess.run(
                ["git", "-C", repo_path, "pull"],
                check=True
            )
