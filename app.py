from flask import Flask, request, jsonify, render_template
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)

def process_frame(frame):
    # Dummy processing for demonstration
    # Implement your actual model inference here
    result = np.random.choice(['Come Closer', 'Perfect Position', 'Too Close'])
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame_route():
    if 'frame' not in request.files:
        return jsonify({'message': 'No frame uploaded'})

    frame_file = request.files['frame']
    frame = Image.open(BytesIO(frame_file.read()))

    # Convert PIL Image to numpy array
    frame_np = np.array(frame)

    # Process the frame using your model
    result = process_frame(frame_np)
    
    return jsonify({'message': result})

if __name__ == "__main__":
    app.run(debug=True)