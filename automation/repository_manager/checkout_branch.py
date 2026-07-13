"""
checkout_branch.py

Checkout configured branch for every repository.
"""

import os
import yaml
import subprocess


class CheckoutBranch:

    def __init__(self):
        self.workspace = "workspace"
        self.config_file = "config/projects.yaml"

    def checkout_all(self):

        with open(self.config_file, "r") as file:
            projects = yaml.safe_load(file)["projects"]

        for project in projects:

            name = project["name"]
            branch = project["branch"]

            repo_path = os.path.join(self.workspace, name)

            if not os.path.exists(repo_path):
                continue

            print(f"Checking out {branch} for {name}")

            subprocess.run(
                ["git", "-C", repo_path, "checkout", branch],
                check=True
            )
