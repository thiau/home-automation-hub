import os
import requests
from cloudant.client import Cloudant
from server.pipeline.pipeline_step import PipelineStep


class UpdateConfigDbStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.title = "Cloud configs updated successfully!"
        self.value = None

        # Get Cloudant Credentials
        self.cloudant_username = os.getenv("CLOUDANT_USERNAME")
        self.cloudant_password = os.getenv("CLOUDANT_PASSWORD")

        # Create Cloudant Instance
        self.cloudant = Cloudant.iam(
            self.cloudant_username, self.cloudant_password, connect=True)

    def get_cloudant_doc(self, database, doc_id):
        my_database = self.cloudant[database]
        document = my_database[doc_id]
        return document

    @staticmethod
    def _get_ngrok_hostname():
        response = requests.get("http://localhost:4040/api/tunnels")
        hostname = response.json().get("tunnels")[0].get("public_url")
        return hostname

    def run(self):
        doc = self.get_cloudant_doc(database="config", doc_id="raspberry_config")
        doc["ngrok_hostname"] = self._get_ngrok_hostname()
        doc.save()
