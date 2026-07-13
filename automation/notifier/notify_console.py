"""
notify_console.py

Console notifications for the OSS Audit Platform.
"""

from datetime import datetime


class ConsoleNotifier:

    @staticmethod
    def info(message):
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"[INFO] {message}"
        )

    @staticmethod
    def success(message):
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"[SUCCESS] {message}"
        )

    @staticmethod
    def warning(message):
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"[WARNING] {message}"
        )

    @staticmethod
    def error(message):
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"[ERROR] {message}"
        )
