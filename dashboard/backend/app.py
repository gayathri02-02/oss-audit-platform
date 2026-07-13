"""
app.py

Entry point for the OSS Audit Platform Dashboard Backend.
"""

from flask import Flask
from routes import dashboard_routes


class DashboardApplication:

    def __init__(self):

        self.app = Flask(__name__)

        self.configure()

    def configure(self):

        #
        # Register Blueprint
        #

        self.app.register_blueprint(
            dashboard_routes
        )

    def run(self):

        self.app.run(

            host="0.0.0.0",

            port=5000,

            debug=True

        )


if __name__ == "__main__":

    dashboard = DashboardApplication()

    dashboard.run()
