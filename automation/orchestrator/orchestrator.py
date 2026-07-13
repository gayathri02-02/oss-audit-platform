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
from automation.notifier.notify_console import ConsoleNotifier
from automation.orchestrator.pipeline import Pipeline
from automation.orchestrator.workflow import Workflow


class Orchestrator:

    def __init__(self):
        self.pipeline = Pipeline()
        self.workflow = Workflow()

    def run(self):

        ConsoleNotifier.info("OSS Audit Pipeline Started")

        phases = self.pipeline.get_pipeline()

        for phase in phases:

            ConsoleNotifier.info(f"Executing Phase : {phase}")

            success = self.workflow.execute(phase)
            print(f"Completed : {phase}")

            if not success:
                ConsoleNotifier.error(f"Pipeline Failed : {phase}")
                return False

        ConsoleNotifier.success("OSS Audit Pipeline Completed")

        return True
