from flask import Flask
from flask import jsonify
# my first flask app, fun fun

app = Flask(__name__)

@app.route ("/")
def index():
    response_data = {}
    response_data['message'] = "welcome"
    response_data['status'] = "success"
    response = jsonify(response_data)
    return response
