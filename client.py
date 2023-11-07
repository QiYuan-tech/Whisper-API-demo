import requests

# server host
url = "http://127.0.0.1:7860/whisper"
# files path
file_path = "examples/en.mp3"

# Send post
# If you choose whisper model, you can:
files = {'file': (file_path, open(file_path, 'rb'))}
data = {'model_type': 'base'}
response = requests.post(url, files=files, data=data)
print(response.json())


# If you don't choose whisper model, you can:
#files = {'file': (file_path, open(file_path, 'rb'))}
#response = requests.post(url, files=files)
#print(response.json())

