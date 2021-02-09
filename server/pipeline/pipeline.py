
class Pipeline:
    def __init__(self, slack_channel):
        self.pipeline = list()
        self.channel = channel

    def add_step(self, step):
        self.pipeline.append(step)

    def run(self):
        print(self.pipeline)
    