"""
pipeline.py

Defines the execution order of the OSS Audit Platform.
"""


class Pipeline:

    def __init__(self):

        self.pipeline = [

            "Clone Repository",

            "Generate SBOM",

            "Generate CBOM",

            "Generate AI Report",

            "Save Artifacts",

            "Update Dashboard",

            "Send Notification"

        ]

    def get_pipeline(self):
        return self.pipeline
