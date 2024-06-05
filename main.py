import os

import requests
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


def query_uptimekuma():
    return {"is": "ok"}


@app.route("/endpoint/", methods=["GET"])
@cross_origin()
def status():
    return jsonify(query_uptimekuma())


if __name__ == "__main__":
    port = int(os.getenv('UKH_PORT', 8099))
    app.run(host="0.0.0.0", port=port)

