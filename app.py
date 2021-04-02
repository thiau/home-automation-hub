###
# @TODO: Use this as a hub to turn the tv on
###

from server import app
from server.routes import ui_routes, status_routes, pipeline_routes


app.run(port=5000, debug=True)
