# app.py
from flask import Flask, request, jsonify, render_template
import os
from detection import detect_plant_diseases
import logging
import uuid

app = Flask(__name__)

# Create a directory for temporary files if it doesn't exist
os.makedirs('temp', exist_ok=True)

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_disease():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    
    # Generate a unique temporary file name
    temp_filename = os.path.join('temp', f"{uuid.uuid4()}.jpg")
    image.save(temp_filename)

    # Call the detection logic
    results = detect_plant_diseases(temp_filename)

    # Remove the temporary image file after processing
    os.remove(temp_filename)

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run()
    
    # app.run(host='0.0.0.0', port=5000, debug=False)

