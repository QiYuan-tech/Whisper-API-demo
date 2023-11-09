from flask import Flask, abort, request
from flask_cors import CORS
from tempfile import NamedTemporaryFile
import whisper
import torch
import argparse
import time

app = Flask(__name__)
CORS(app)

def whisper_model(model_type="large"):
    # Check if NVIDIA GPU is available
    torch.cuda.is_available()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the Whisper model
    model = whisper.load_model(model_type, device=DEVICE, download_root="./")
    return model

@app.route("/")
def hello():
    return "Welcome to the Voice-to-Text (Whisper) API"

@app.route('/whisper', methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)
    # chose model. `tiny`, `base`, etc.
    if not request.form:
        model_type = "large"
    if request.form:
        model_type = request.form['model_type']
    
    # Load the Whisper model
    start_time = time.time()
    model = whisper_model(model_type)
    end_time = time.time()
    formatted_time = "{:.2f}s".format(end_time-start_time)
    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        result = model.transcribe(temp.name)
        # Now we can store the result object for this file.
        results.append({
            'transcript': result['text'],
            'model_type': str(model_type),
            'time': formatted_time
        })

    # This will be automatically converted to JSON.
    return {'results': results}

if __name__ == "__main__":
    # Whisper Server Parameter
    parser = argparse.ArgumentParser(description='Whisper Server Parameter')
    parser.add_argument('--port', type=str, help='Server Port', default='7860')
    parser.add_argument('--host', type=str, help='Server Host', default='127.0.0.1')
    args = vars(parser.parse_args())
    
    app.run(debug=True, threaded=True, host=args['host'], port=args['port'])