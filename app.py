from flask import Flask, request, jsonify, send_file, Response
from pathlib import Path
import json
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import os


app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response


@app.route("/ping")
def ping():
    file = Path("/tmp/OK")
    if file.is_file():
        return "OK"
    else:
        return Response("Health check fails", status=503, mimetype='application/json')

@app.route("/img")
def get_image():
    return send_file("ok.gif", mimetype='image/gif')

if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    port = int(os.environ.get("PORT", 5000)) # <-----
    app.run(debug=True, host='0.0.0.0', port=port, processes=3)