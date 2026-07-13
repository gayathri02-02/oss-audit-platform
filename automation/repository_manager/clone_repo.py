"""
clone_repo.py

Clone all repositories defined in config/projects.yaml
"""

import os
import yaml
import subprocess


class CloneRepository:

    def __init__(self):
        self.config_file = "config/projects.yaml"
        self.workspace = "workspace"

    def load_projects(self):
        with open(self.config_file, "r") as file:
            config = yaml.safe_load(file)

        return config["projects"]

    def clone_all(self):

        os.makedirs(self.workspace, exist_ok=True)

        projects = self.load_projects()

        for project in projects:

            if not project.get("enabled", True):
                continue

            repo = project["repo"]
            name = project["name"]

            destination = os.path.join(self.workspace, name)

            if os.path.exists(destination):
                print(f"{name} already exists.")
                continue

            print(f"Cloning {name}")

            subprocess.run([
                "git",
                "clone",
                repo,
                destination
            ], check=True)
