"""
parse_scanoss.py

Parse SCANOSS output.
"""

import json


class ScanOSSParser:

    def parse(self, file_path):

        with open(file_path, "r") as file:

            data = json.load(file)

        return data
