"""
models.py

Data models used by the Dashboard Backend.
"""


class Project:

    def __init__(
        self,
        project_name,
        repository,
        last_scan,
        compliance_score
    ):

        self.project_name = project_name

        self.repository = repository

        self.last_scan = last_scan

        self.compliance_score = compliance_score

    def to_dict(self):

        return {

            "project_name": self.project_name,

            "repository": self.repository,

            "last_scan": self.last_scan,

            "compliance_score": self.compliance_score

        }


class SBOM:

    def __init__(
        self,
        project_name,
        sbom_path,
        generated_on
    ):

        self.project_name = project_name

        self.sbom_path = sbom_path

        self.generated_on = generated_on

    def to_dict(self):

        return {

            "project_name": self.project_name,

            "sbom_path": self.sbom_path,

            "generated_on": self.generated_on

        }


class CBOM:

    def __init__(
        self,
        project_name,
        cbom_path,
        generated_on
    ):

        self.project_name = project_name

        self.cbom_path = cbom_path

        self.generated_on = generated_on

    def to_dict(self):

        return {

            "project_name": self.project_name,

            "cbom_path": self.cbom_path,

            "generated_on": self.generated_on

        }


class Report:

    def __init__(
        self,
        project_name,
        report_path,
        generated_on
    ):

        self.project_name = project_name

        self.report_path = report_path

        self.generated_on = generated_on

    def to_dict(self):

        return {

            "project_name": self.project_name,

            "report_path": self.report_path,

            "generated_on": self.generated_on

        }


class DashboardSummary:

    def __init__(
        self,
        projects,
        sboms,
        cboms,
        reports,
        compliance
    ):

        self.projects = projects

        self.sboms = sboms

        self.cboms = cboms

        self.reports = reports

        self.compliance = compliance

    def to_dict(self):

        return {

            "projects": self.projects,

            "sboms": self.sboms,

            "cboms": self.cboms,

            "reports": self.reports,

            "compliance": self.compliance

        }
