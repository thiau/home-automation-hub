
# Import Pipeline Steps
from server.helpers.pipeline.pipeline import Pipeline
from server.helpers.pipeline.steps.initial_step import InitialStep
from server.helpers.pipeline.steps.get_ip_step import GetIPAddressStep
from server.helpers.pipeline.steps.start_ngrok_step import StartNgrokStep
from server.helpers.pipeline.steps.update_config_db_step import (
    UpdateConfigDbStep)


def start():
    pipeline = Pipeline()
    pipeline.add_step(InitialStep)
    pipeline.add_step(GetIPAddressStep)
    pipeline.add_step(StartNgrokStep)
    pipeline.add_step(UpdateConfigDbStep)
    pipeline.run()
