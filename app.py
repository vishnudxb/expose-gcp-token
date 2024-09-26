from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def expose_token():
    # Metadata URL to get the access token
    metadata_url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
    headers = {'Metadata-Flavor': 'Google'}
    
    # Fetch the access token from metadata server
    token_response = requests.get(metadata_url, headers=headers)
    token = token_response.json()
    
    # Expose the token as a JSON response
    return jsonify(token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

