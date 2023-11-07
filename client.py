import requests

# files
file_path = "examples/en.mp3"

# Server Host
url = "http://127.0.0.1:7860/whisper"

files = {'file': (file_path, open(file_path, 'rb'))}
# Send post
response = requests.post(url, files=files)
print(response.json())