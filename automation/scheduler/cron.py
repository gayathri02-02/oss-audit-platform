"""
cron.py

Local scheduler for the OSS Audit Platform.

This module allows the pipeline to be executed on a schedule
outside of GitHub Actions (for local testing or future deployment).

GitHub Actions remains the primary scheduler.
"""

import time
import schedule

from automation.scheduler.scheduler import Scheduler


class CronScheduler:
    """Runs the OSS Audit Pipeline based on a local schedule."""

    def __init__(self):
        self.scheduler = Scheduler()

    def weekly(self):
        """Execute the pipeline once."""
        self.scheduler.run()

    def start(self):
        """Start the local scheduler."""

        # Every Friday at 02:00
        schedule.every().friday.at("02:00").do(self.weekly)

        print("=" * 60)
        print("Local Scheduler Started")
        print("Waiting for scheduled jobs...")
        print("=" * 60)

        while True:
            schedule.run_pending()
            time.sleep(30)


if __name__ == "__main__":
    CronScheduler().start()
