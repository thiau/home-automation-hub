import requests
from server import app, jsonify

# implement a base function to get the status


def is_ngrok_running():
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        value = response.json().get("tunnels")[0].get("public_url")

        if value:
            return True
        else:
            return False
    except Exception as error:
        return False


def is_samsung_running():
    try:
        response = requests.get("http://localhost:3001/app/status")
        value = response.json()

        if value:
            return True
        else:
            return False
    except Exception as error:
        return False


@app.route("/status/ngrok", methods=["GET"])
def status_ngrok():
    return jsonify(component="NGROK", status=is_ngrok_running())


@app.route("/status/samsung", methods=["GET"])
def status_samsung():
    return jsonify(component="Samsung REST", status=is_samsung_running())
