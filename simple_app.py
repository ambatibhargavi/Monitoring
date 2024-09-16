from flask import Flask
from prometheus_client import start_http_server, Summary, Counter, generate_latest

app = Flask(__name__)

# Create a metric to track the number of requests
REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    start_http_server(5001)
    app.run(host='0.0.0.0', port=4000)
