import os
import time
import requests
from subprocess import call
from server.pipeline.pipeline_step import PipelineStep


class StartNgrokStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.title = "NGROK Service"
        self.value = None

    def run(self):
        ngrok_base = os.getenv("RASP_NGROK_PATH")
        call(f"{ngrok_base}/ngrok http 5000 > /dev/null &", shell=True)
        time.sleep(10)
        response = requests.get("http://localhost:4040/api/tunnels")
        self.value = response.json().get("tunnels")[0].get("public_url")
