"""
Unit tests for the Dashboard Backend.
"""

import unittest

from dashboard.backend.app import app


class TestDashboard(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()

        self.client.testing = True

    def test_dashboard_application_exists(self):

        self.assertIsNotNone(app)

    def test_dashboard_endpoint(self):

        response = self.client.get("/api/dashboard")

        self.assertEqual(response.status_code, 200)

    def test_projects_endpoint(self):

        response = self.client.get("/api/projects")

        self.assertEqual(response.status_code, 200)

    def test_sboms_endpoint(self):

        response = self.client.get("/api/sboms")

        self.assertEqual(response.status_code, 200)

    def test_cboms_endpoint(self):

        response = self.client.get("/api/cboms")

        self.assertEqual(response.status_code, 200)

    def test_reports_endpoint(self):

        response = self.client.get("/api/reports")

        self.assertEqual(response.status_code, 200)

    def test_analytics_endpoint(self):

        response = self.client.get("/api/analytics")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":

    unittest.main()
