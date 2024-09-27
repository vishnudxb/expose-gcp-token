import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def expose_token():
    # GCP metadata server URL to get the access token
    metadata_url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
    headers = {'Metadata-Flavor': 'Google'}
    
    # Fetch the access token from the metadata server
    token_response = requests.get(metadata_url, headers=headers)
    token = token_response.json()

    # Expose the token as JSON
    return jsonify(token)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use the correct port
    app.run(host='0.0.0.0', port=port)
