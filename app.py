
from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    logging.debug("{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached")
    app.logger.info('Successfully reached status')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    logging.debug("{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached")
    app.logger.info('Successfully reached metrics')
    return response

@app.route("/")
def hello():
    app.logger.info('Successfully reached main')
    logging.debug("{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached")
    return "Hello World!  this is wild"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
