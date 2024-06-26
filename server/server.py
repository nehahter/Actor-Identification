from flask import Flask, request, jsonify
from flask_cors import CORS   # Import CORS from flask_cors module
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Actor Identification")
    util.load_saved_artifacts()
    app.run(port=5000, debug=True)
