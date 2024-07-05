from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

# Your Flask API routes go here

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
