import json
from dotenv import load_dotenv
from server.pipeline.pipeline import Pipeline
from server.pipeline.steps.initial_step import InitialStep
from server.pipeline.steps.get_ip_step import GetIPAddressStep

load_dotenv()

pipeline = Pipeline()
pipeline.add_step(InitialStep)
pipeline.add_step(GetIPAddressStep)
pipeline.run()