"""
database.py

SQLite database manager for the OSS Audit Platform Dashboard.
"""

import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        self.database_directory = Path("storage/database")

        self.database_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        self.database_file = (
            self.database_directory /
            "dashboard.db"
        )

        self.connection = sqlite3.connect(
            self.database_file,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        #
        # Projects Table
        #

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS projects (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_name TEXT UNIQUE,

            repository TEXT,

            last_scan TEXT,

            compliance_score INTEGER

        )

        """)

        #
        # Reports Table
        #

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_name TEXT,

            report_path TEXT,

            generated_on TEXT

        )

        """)

        #
        # SBOM Table
        #

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS sboms (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_name TEXT,

            sbom_path TEXT,

            generated_on TEXT

        )

        """)

        #
        # CBOM Table
        #

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS cboms (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_name TEXT,

            cbom_path TEXT,

            generated_on TEXT

        )

        """)

        self.connection.commit()

    def execute(
        self,
        query,
        parameters=()
    ):

        self.cursor.execute(
            query,
            parameters
        )

        self.connection.commit()

    def fetch_all(
        self,
        query,
        parameters=()
    ):

        self.cursor.execute(
            query,
            parameters
        )

        return self.cursor.fetchall()

    def fetch_one(
        self,
        query,
        parameters=()
    ):

        self.cursor.execute(
            query,
            parameters
        )

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()
