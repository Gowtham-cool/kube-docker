from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {os.getenv('ENV')} environment"

app.run(host="0.0.0.0", port=8080)
