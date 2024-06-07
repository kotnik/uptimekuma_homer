import os
import sys

import requests
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from prometheus_client.parser import text_string_to_metric_families


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


def query_uptimekuma():
    # Prepare
    host = os.getenv('UKH_HOST', None)
    api_key = os.getenv('UKH_API_KEY', None)
    if host is None or api_key is None:
        raise Exception('Missing credentials')
    if not host.endswith('/'):
        host = f"{host}/"
    host_metrics = f"{host}metrics"

    # Query
    r = requests.get(host_metrics, auth=('', api_key))
    if r.status_code != 200:
        raise Exception('Failed to fetch')

    # Parse
    services = {
        "total": 0,
        "up": 0,
        "down": 0,
        "pending": 0,
        "maintenance": 0,
    }
    for family in text_string_to_metric_families(r.text):
        if family.name != 'monitor_status':
            continue
        for sample in family.samples:
            value = int(sample.value)
            services['total'] += 1
            # (1 = UP, 0= DOWN, 2= PENDING, 3= MAINTENANCE)
            if value == 0:
                services['down'] += 1
            elif value == 1:
                services['up'] += 1
            elif value == 2:
                services['pending'] += 1
            elif value == 3:
                services['maintenance'] += 1
    assert(services['total'] == (services['down'] + services['up'] + services['pending'] + services['maintenance']))

    # Prepare output
    ret = {}
    if services['down'] > 0:
        ret['style'] = 'is-danger'
        ret['title'] = 'Service disruption'
    else:
        ret['style'] = 'is-success'
        ret['title'] = 'Everything is up and running'
    ret['content'] = f"<b>Online {services['up']} / {services['total']}. Check <a href={host} target=_blank>here</a> for more info. </br> <p>"
    return ret


@app.route("/endpoint/", methods=["GET"])
@cross_origin()
def status():
    return jsonify(query_uptimekuma())


if __name__ == "__main__":
    port = int(os.getenv('UKH_PORT', 8099))
    app.run(host="0.0.0.0", port=port)

