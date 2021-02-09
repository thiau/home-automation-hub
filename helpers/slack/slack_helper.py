import requests
import json
import logging
import os

class Slack:
    def __init__(self):
        self.api_endpoint = os.getenv("SLACK_API_ENDPOINT")
        self.api_token = os.getenv("SLACK_API_TOKEN")
        self.default_channel = os.getenv("SLACK_DEFAULT_CHANNEL")

        # Logging setup
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')


    def build_headers(self):
        headers = dict()
        headers["Authorization"] = f'Bearer {self.api_token}'
        headers["Content-Type"] = 'application/json'
        return headers


    def build_payload(self, message, channel=None, ts=None):
        payload = dict()
        payload["channel"] = channel
        payload["text"] = message
        payload["thread_ts"] = ts
        return json.dumps(payload)
    

    def send_message(self, message=None, channel=None, ts=None, custom_payload=None):
        try:
            channel = self.default_channel if not channel else channel
            payload = custom_payload if custom_payload else self.build_payload(message, channel, ts)
            headers = self.build_headers()
        
            response = requests.post(self.api_endpoint, headers=headers, data=payload)
            response = json.loads(response.text)
            
            if not response.get("ok"):
                raise Exception(response.get("error"))
        except Exception as err:
            logging.error("Error on sending slack message")
            logging.error(err)
