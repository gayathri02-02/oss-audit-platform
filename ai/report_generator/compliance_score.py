"""
compliance_score.py

Calculates the compliance score for the OSS Audit Report.
"""


class ComplianceScore:

    def __init__(self):
        pass

    def calculate(
        self,
        sbom_data,
        cbom_data
    ):

        score = 100

        findings = []

        #
        # SBOM Validation
        #

        if not sbom_data:

            score -= 30

            findings.append(
                "SBOM is missing."
            )

        #
        # CBOM Validation
        #

        if not cbom_data:

            score -= 30

            findings.append(
                "CBOM is missing."
            )

        #
        # Compliance Status
        #

        if score >= 90:

            status = "Excellent"

        elif score >= 75:

            status = "Good"

        elif score >= 60:

            status = "Fair"

        else:

            status = "Poor"

        return {

            "score": score,

            "status": status,

            "findings": findings

        }
