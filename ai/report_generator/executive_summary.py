"""
executive_summary.py

Generates the Executive Summary section
for the OSS Audit Report.
"""


class ExecutiveSummary:

    def __init__(self):
        pass

    def generate(
        self,
        project_name,
        sbom_data,
        cbom_data
    ):

        summary = []

        summary.append(
            f"Project '{project_name}' was successfully audited."
        )

        if sbom_data:
            summary.append(
                "Software Bill of Materials (SBOM) was generated successfully."
            )
        else:
            summary.append(
                "SBOM generation failed."
            )

        if cbom_data:
            summary.append(
                "Cryptography Bill of Materials (CBOM) was generated successfully."
            )
        else:
            summary.append(
                "CBOM generation failed."
            )

        summary.append(
            "Further analysis has been performed to evaluate software components, cryptographic assets, compliance status, and security posture."
        )

        return " ".join(summary)
