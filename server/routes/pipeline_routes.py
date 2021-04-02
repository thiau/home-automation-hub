from server import app, jsonify
from server.factory.pipeline import start


@app.route("/pipeline/start")
def pipeline_start():
    start()
    return "Started"
