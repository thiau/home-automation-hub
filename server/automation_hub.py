import json
import helpers.raspberry.network_helper as networking
from helpers.slack.slack_helper import Slack

# @TODO: Create a Pipeline of tasks, where each task appends the field object

class AutomationHub:
    def __init__(self):
        self.ip_address = networking.get_ip_address()
        self.hostname = None
        self.slack = Slack()

    def send_initial_message(self):
        payload = {
            "channel": "C01M8BY9NEA",
            "attachments": [
                {
                    "mrkdwn_in": ["text"],
                    "color": "warning",
                    "author_name": "Home Automation Bot",
                    "author_icon": "https://placeimg.com/16/16/people",
                    "fields": [
                        {
                            "value": "Starting Home Automation Hub",
                            "short": False
                        },
                        {   
                            "title": "IP Address",
                            "value": self.ip_address,
                            "short": False
                        }
                    ],
                    "footer": "home automation app",
                }
            ]
        }

        payload = json.dumps(payload)
        self.slack.send_message(custom_payload=payload)

    def start(self):
        self.send_initial_message()