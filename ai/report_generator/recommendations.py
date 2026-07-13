"""
recommendations.py

Generates recommendations for the OSS Audit Report
based on SBOM and CBOM analysis.
"""


class Recommendations:

    def __init__(self):
        pass

    def generate(
        self,
        sbom_data,
        cbom_data
    ):

        recommendations = []

        #
        # SBOM Recommendations
        #

        if not sbom_data:

            recommendations.append(
                "Generate a valid Software Bill of Materials (SBOM) before software release."
            )

        else:

            recommendations.append(
                "Review all third-party software components for license compliance."
            )

            recommendations.append(
                "Keep the SBOM updated for every software release."
            )

        #
        # CBOM Recommendations
        #

        if not cbom_data:

            recommendations.append(
                "Generate a Cryptography Bill of Materials (CBOM) to identify cryptographic assets."
            )

        else:

            recommendations.append(
                "Review cryptographic libraries and algorithms for organizational compliance."
            )

            recommendations.append(
                "Replace deprecated or weak cryptographic algorithms where applicable."
            )

            recommendations.append(
                "Ensure cryptographic libraries are updated to supported versions."
            )

        #
        # General Recommendations
        #

        recommendations.append(
            "Perform OSS compliance audits on a weekly basis."
        )

        recommendations.append(
            "Maintain historical SBOMs and CBOMs for traceability."
        )

        recommendations.append(
            "Automate compliance checks within the CI/CD pipeline."
        )

        recommendations.append(
            "Review security vulnerabilities before production deployment."
        )

        return recommendations
