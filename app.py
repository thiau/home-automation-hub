import json
from dotenv import load_dotenv
from server.pipeline.pipeline import Pipeline
from server.pipeline.steps.initial_step import InitialStep
from server.pipeline.steps.get_ip_step import GetIPAddressStep
from server.pipeline.steps.start_ngrok_step import StartNgrokStep
from server.pipeline.steps.update_config_db_step import UpdateConfigDbStep

load_dotenv()

pipeline = Pipeline()
pipeline.add_step(InitialStep)
pipeline.add_step(GetIPAddressStep)
pipeline.add_step(StartNgrokStep)
pipeline.add_step(UpdateConfigDbStep)
pipeline.run()
