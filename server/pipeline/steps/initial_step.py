from server.pipeline.pipeline_step import PipelineStep


class InitialStep(PipelineStep):
    def __init__(self):
        super().__init__()
        self.value = "Starting Home Automation Hub"
