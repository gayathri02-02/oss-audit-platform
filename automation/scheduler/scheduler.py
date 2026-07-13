"""
scheduler.py

Starts the OSS Audit Pipeline.
This file acts as the entry point for the automation workflow.
"""

from automation.orchestrator.orchestrator import Orchestrator


class Scheduler:
    """Starts the automation pipeline."""

    def __init__(self):
        self.orchestrator = Orchestrator()

    def run(self):
        print("=" * 60)
        print("Starting OSS Audit Automation Pipeline...")
        print("=" * 60)

        self.orchestrator.run()

        print("=" * 60)
        print("Pipeline Completed Successfully.")
        print("=" * 60)


if __name__ == "__main__":
    Scheduler().run()
