"""
export_pdf.py

Exports the OSS Audit Report as a PDF.
"""

from pathlib import Path
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


class PDFExporter:

    def __init__(self):

        self.output_directory = Path("storage/reports")

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        self.styles = getSampleStyleSheet()

    def export(
        self,
        project_name,
        report
    ):

        project_directory = self.output_directory / project_name

        project_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = project_directory / "report.pdf"

        document = SimpleDocTemplate(
            str(output_file)
        )

        elements = []

        #
        # Title
        #

        elements.append(
            Paragraph(
                f"<b>OSS Audit Report</b>",
                self.styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        #
        # Project
        #

        elements.append(
            Paragraph(
                f"<b>Project:</b> {report['project']}",
                self.styles["Heading2"]
            )
        )

        elements.append(Spacer(1, 12))

        #
        # Executive Summary
        #

        elements.append(
            Paragraph(
                "<b>Executive Summary</b>",
                self.styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                report["executive_summary"],
                self.styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 12))

        #
        # Compliance Score
        #

        score = report["compliance_score"]

        elements.append(
            Paragraph(
                "<b>Compliance Score</b>",
                self.styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Score : {score['score']}",
                self.styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Status : {score['status']}",
                self.styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 12))

        #
        # Findings
        #

        if score["findings"]:

            elements.append(
                Paragraph(
                    "<b>Findings</b>",
                    self.styles["Heading2"]
                )
            )

            for finding in score["findings"]:

                elements.append(
                    Paragraph(
                        f"• {finding}",
                        self.styles["BodyText"]
                    )
                )

            elements.append(Spacer(1, 12))

        #
        # Crypto Analysis
        #

        crypto = report["crypto_analysis"]

        elements.append(
            Paragraph(
                "<b>Cryptographic Analysis</b>",
                self.styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Status : {crypto['status']}",
                self.styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Crypto Components : {crypto['total_crypto_components']}",
                self.styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 12))

        #
        # Recommendations
        #

        elements.append(
            Paragraph(
                "<b>Recommendations</b>",
                self.styles["Heading2"]
            )
        )

        for recommendation in report["recommendations"]:

            elements.append(
                Paragraph(
                    f"• {recommendation}",
                    self.styles["BodyText"]
                )
            )

        document.build(elements)

        print(f"PDF exported : {output_file}")

        return output_file
