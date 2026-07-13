"""
generate_report.py

Main AI Report Generator

This module orchestrates the complete report generation process.

Workflow:

SBOM
   │
CBOM
   │
Executive Summary
   │
Compliance Score
   │
Crypto Analysis
   │
Recommendations
   │
Export PDF
"""

from ai.report_generator.executive_summary import ExecutiveSummary
from ai.report_generator.compliance_score import ComplianceScore
from ai.report_generator.crypto_analysis import CryptoAnalysis
from ai.report_generator.recommendations import Recommendations
from ai.report_generator.export_pdf import PDFExporter


class ReportGenerator:

    def __init__(self):

        self.summary = ExecutiveSummary()
        self.score = ComplianceScore()
        self.crypto = CryptoAnalysis()
        self.recommendation = Recommendations()
        self.pdf = PDFExporter()

    def generate(
        self,
        project_name,
        sbom_data,
        cbom_data
    ):

        print(f"\nGenerating AI Report : {project_name}")

        report = {

            "project": project_name,

            "executive_summary":
                self.summary.generate(
                    project_name,
                    sbom_data,
                    cbom_data
                ),

            "compliance_score":
                self.score.calculate(
                    sbom_data,
                    cbom_data
                ),

            "crypto_analysis":
                self.crypto.analyze(
                    cbom_data
                ),

            "recommendations":
                self.recommendation.generate(
                    sbom_data,
                    cbom_data
                )
        }

        output = self.pdf.export(
            project_name,
            report
        )

        print("AI Report Generated Successfully")

        return output
