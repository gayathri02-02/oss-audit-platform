"""
utils.py

Utility functions for the OSS Audit Platform Dashboard.
"""

from pathlib import Path
from datetime import datetime


class DashboardUtils:

    @staticmethod
    def file_exists(path):

        return Path(path).exists()

    @staticmethod
    def create_directory(path):

        Path(path).mkdir(

            parents=True,

            exist_ok=True

        )

    @staticmethod
    def current_timestamp():

        return datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    @staticmethod
    def current_date():

        return datetime.now().strftime(

            "%Y-%m-%d"

        )

    @staticmethod
    def file_size(path):

        file = Path(path)

        if not file.exists():

            return 0

        return file.stat().st_size

    @staticmethod
    def list_files(directory):

        directory = Path(directory)

        if not directory.exists():

            return []

        return [

            file.name

            for file in directory.iterdir()

            if file.is_file()

        ]

    @staticmethod
    def list_directories(directory):

        directory = Path(directory)

        if not directory.exists():

            return []

        return [

            folder.name

            for folder in directory.iterdir()

            if folder.is_dir()

        ]

    @staticmethod
    def format_percentage(value):

        return f"{value:.2f}%"

    @staticmethod
    def calculate_compliance_score(scores):

        if not scores:

            return 0

        return round(

            sum(scores) / len(scores),

            2

        )
