"""
parse_cbom.py
"""

import json


class CBOMParser:

    def parse(self, file):

        with open(file, "r") as f:

            return json.load(f)
