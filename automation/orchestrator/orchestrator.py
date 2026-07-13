"""
orchestrator.py

Main Orchestrator for the OSS Audit Platform.

Responsibilities:
1. Read pipeline
2. Execute workflows
3. Monitor execution
4. Handle failures
5. Display execution status
"""

from automation.orchestrator.pipeline import Pipeline
from automation.orchestrator.workflow import Workflow


class Orchestrator:

    def __init__(self):
        self.pipeline = Pipeline()
        self.workflow = Workflow()

    def run(self):

        print("\n======================================")
        print("      OSS Audit Pipeline Started")
        print("======================================\n")

        phases = self.pipeline.get_pipeline()

        for phase in phases:

            print(f"\nExecuting {phase}")

            success = self.workflow.execute(phase)
            print(f"Completed : {phase}")

            if not success:
                print(f"\nPipeline Failed at {phase}")
                return False

        print("\n======================================")
        print(" OSS Audit Pipeline Completed")
        print("======================================\n")

        return True
