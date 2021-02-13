import os
import requests
from cloudant.client import Cloudant
from server.pipeline.pipeline_step import PipelineStep


class UpdateConfigDbStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.title = "Cloud configs updated successfully!"
        self.value = None

        self.cloudant = Cloudant.iam("2f6cd0a9-534d-4350-9b14-2d0011dd5a17-bluemix", "uF0iS07PaTs4H_o8b-kqdntz9C5bJayiq4pSzMDDom9h", connect=True)

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
        doc["test_param"] = self._get_ngrok_hostname()
        doc.save()
