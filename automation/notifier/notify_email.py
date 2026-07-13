"""
notify_email.py

Placeholder for email notifications.
"""


class EmailNotifier:

    def send(
        self,
        subject,
        body,
        recipients
    ):

        print("=" * 60)
        print("EMAIL NOTIFICATION")
        print("=" * 60)

        print(f"Subject : {subject}")
        print(f"Recipients : {recipients}")
        print(body)

        print("=" * 60)

        # Future:
        # SMTP
        # Microsoft Graph
        # Gmail API

        return True
