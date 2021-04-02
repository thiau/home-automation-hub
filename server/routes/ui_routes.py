from server import app, render_template


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")
