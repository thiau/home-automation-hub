from server.pipeline.pipeline_step import PipelineStep
import helpers.raspberry.network_helper as networking


class GetIPAddressStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.title = "IP Address"

    def run(self):
        self.value = networking.get_ip_address()
