from subprocess import call
from server.pipeline.pipeline_step import PipelineStep


class StartNgrokStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.title = "NGROK Service"
        self.value = None

    def run(self):
        # @TODO: Update to full path
        call("./ngrok http 5000 > /dev/null &", shell=True)
