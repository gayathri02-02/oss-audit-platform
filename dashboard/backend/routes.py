"""
routes.py

REST API routes for the OSS Audit Platform Dashboard.
"""

from flask import Blueprint
from flask import jsonify

from services import DashboardService

dashboard_routes = Blueprint(
    "dashboard",
    __name__
)

service = DashboardService()


#
# Dashboard Overview
#

@dashboard_routes.route(
    "/api/dashboard",
    methods=["GET"]
)
def dashboard():

    return jsonify(
        service.get_dashboard_summary()
    )


#
# Projects
#

@dashboard_routes.route(
    "/api/projects",
    methods=["GET"]
)
def projects():

    return jsonify(
        service.get_projects()
    )


#
# SBOM
#

@dashboard_routes.route(
    "/api/sboms",
    methods=["GET"]
)
def sboms():

    return jsonify(
        service.get_sboms()
    )


#
# CBOM
#

@dashboard_routes.route(
    "/api/cboms",
    methods=["GET"]
)
def cboms():

    return jsonify(
        service.get_cboms()
    )


#
# Reports
#

@dashboard_routes.route(
    "/api/reports",
    methods=["GET"]
)
def reports():

    return jsonify(
        service.get_reports()
    )


#
# Analytics
#

@dashboard_routes.route(
    "/api/analytics",
    methods=["GET"]
)
def analytics():

    return jsonify(
        service.get_analytics()
    )
