import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Exposing GCP Token"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Get port from environment
    app.run(host='0.0.0.0', port=port)
