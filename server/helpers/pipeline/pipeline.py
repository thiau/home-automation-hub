import json
import time
import os
from helpers.slack.slack_helper import Slack

# @TODO: Should the slack channel be definied in the Slack class instanciation?
# @TODO: Should I move the slack_message object to another file?
# @TODO: Add error handling


class Pipeline:
    def __init__(self):
        self.slack = Slack()
        self.pipeline_steps = list()
        self.slack_ts = str()
        self.slack_message = {
            "channel": os.getenv("SLACK_DEFAULT_CHANNEL"),
            "attachments": [
                {
                    "mrkdwn_in": ["text"],
                    "color": "warning",
                    "author_name": "Home Automation Bot",
                    "fields": [],
                    "footer": "home automation app",
                }
            ]
        }

    def add_step(self, step):
        self.pipeline_steps.append(step)

    @staticmethod
    def _build_fields(step):
        fields = dict()
        fields["title"] = step.title
        fields["value"] = step.value
        fields["short"] = step.short
        return fields

    def run(self):
        try:
            for pipeline_step in self.pipeline_steps:
                # time.sleep(5)

                # Instanciate and run PipelineStep object
                step = pipeline_step()
                step.run()

                # Build Fields message object
                fields = self._build_fields(step)
                self.slack_message["attachments"][0]["fields"].append(fields)

                # Send or update slack message
                if self.slack_ts:
                    self.slack_message["ts"] = self.slack_ts
                    self.slack.update_message(
                        custom_payload=json.dumps(self.slack_message))
                else:
                    slack_response = self.slack.send_message(
                        custom_payload=json.dumps(self.slack_message))
                    self.slack_ts = slack_response.get("ts")

            # Send finish message
            self.slack_message["attachments"][0]["color"] = "good"
            self.slack.update_message(
                custom_payload=json.dumps(self.slack_message))
        except Exception as e:
            # Send error message
            self.slack_message["attachments"][0]["color"] = "danger"
            self.slack.update_message(
                custom_payload=json.dumps(self.slack_message))
            print(e)
