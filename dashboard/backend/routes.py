"""
routes.py

REST API routes for the OSS Audit Platform Dashboard.
"""

from flask import Blueprint
from flask import jsonify

dashboard_routes = Blueprint(
    "dashboard",
    __name__
)


#
# Dashboard Overview
#

@dashboard_routes.route(
    "/api/dashboard",
    methods=["GET"]
)
def dashboard():

    return jsonify({

        "projects": 0,

        "sboms": 0,

        "cboms": 0,

        "reports": 0,

        "compliance": 0

    })


#
# Projects
#

@dashboard_routes.route(
    "/api/projects",
    methods=["GET"]
)
def projects():

    return jsonify([])


#
# SBOM
#

@dashboard_routes.route(
    "/api/sboms",
    methods=["GET"]
)
def sboms():

    return jsonify([])


#
# CBOM
#

@dashboard_routes.route(
    "/api/cboms",
    methods=["GET"]
)
def cboms():

    return jsonify([])


#
# Reports
#

@dashboard_routes.route(
    "/api/reports",
    methods=["GET"]
)
def reports():

    return jsonify([])


#
# Analytics
#

@dashboard_routes.route(
    "/api/analytics",
    methods=["GET"]
)
def analytics():

    return jsonify({

        "weekly": [],

        "monthly": [],

        "yearly": []

    })
