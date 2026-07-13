"""
services.py

Business logic for the OSS Audit Platform Dashboard.
"""

from pathlib import Path

from database import DatabaseManager


class DashboardService:

    def __init__(self):

        self.database = DatabaseManager()

        self.storage = Path("storage")

    #
    # Dashboard
    #

    def get_dashboard_summary(self):

        projects = self.database.fetch_one(
            "SELECT COUNT(*) AS count FROM projects"
        )

        sboms = self.database.fetch_one(
            "SELECT COUNT(*) AS count FROM sboms"
        )

        cboms = self.database.fetch_one(
            "SELECT COUNT(*) AS count FROM cboms"
        )

        reports = self.database.fetch_one(
            "SELECT COUNT(*) AS count FROM reports"
        )

        compliance = self.database.fetch_one(
            """
            SELECT AVG(compliance_score) AS average
            FROM projects
            """
        )

        return {

            "projects":
                projects["count"],

            "sboms":
                sboms["count"],

            "cboms":
                cboms["count"],

            "reports":
                reports["count"],

            "compliance":
                round(
                    compliance["average"], 2
                ) if compliance["average"] else 0

        }

    #
    # Projects
    #

    def get_projects(self):

        rows = self.database.fetch_all(
            "SELECT * FROM projects"
        )

        return [dict(row) for row in rows]

    #
    # SBOMs
    #

    def get_sboms(self):

        rows = self.database.fetch_all(
            "SELECT * FROM sboms"
        )

        return [dict(row) for row in rows]

    #
    # CBOMs
    #

    def get_cboms(self):

        rows = self.database.fetch_all(
            "SELECT * FROM cboms"
        )

        return [dict(row) for row in rows]

    #
    # Reports
    #

    def get_reports(self):

        rows = self.database.fetch_all(
            "SELECT * FROM reports"
        )

        return [dict(row) for row in rows]

    #
    # Analytics
    #

    def get_analytics(self):

        return {

            "weekly": [],

            "monthly": [],

            "yearly": []

        }
