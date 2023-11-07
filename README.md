Welcome to the Voice-to-Text (Whisper) API

## Setup

First, you must install Python dependencies:
```python
pip install -r requirements.txt
```

It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Usage

### Start Server

```python
python server.py
```

You can set the `host` and `port` of the service:
```python
python server.py --host 0.0.0.0 --port 8888
```

### Use Server

```bash
curl -F "file=@examples/en.mp3" http://127.0.0.1:7860/whisper
```

You should do this when you want to use other models:
```bash
# Use `base`
curl -X POST -F "file=@examples/en.mp3" -F "model_type=base" http://127.0.0.1:7860/whisper

# Use `base.en`
curl -X POST -F "file=@examples/en.mp3" -F "model_type=base.en" http://127.0.0.1:7860/whisper
```

Comparison of different models:
|`model_type`|Required VRAM|Parameters|Relative speed|
|:-|:-|:-|:-|
|`tiny.en` or `tiny`|~1 GB|39 M|~32x|
|`base.en` or `base`|~1 GB|74 M|~16x|
|`small.en` or `small`|~2 GB|244 M|~6x|
|`medium.en` or `medium`|~5 GB|769 M|~2x|
|`large`|~10 GB|1550 M|1x|

The `.en` models for English-only applications tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models.

You can also use `python` to send post requests:

```python
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
```

## Examples

```bash
$ curl -X POST -F "file=@en.mp3" -F "model_type=base.en" http://127.0.0.1:7860/whisper
$
$ {
  "results": [
    {
      "model_type": "base",
      "time": "0.90s",
      "transcript": " Hello, my name is Sarah. I'm 25 years old and I come from a small town in California. I currently work as a graphic designer and I have a passion for creating visually appealing and innovative designs. I graduated from the University of California where I earned a bachelor's degree in graphic design and I've been working in the design industry for about three years. In my free time, I enjoy hiking in the beautiful California wilderness, experimenting with new recipes in the kitchen and playing the guitar. I also love photography and often capture the beauty of nature during my hikes."
    }
  ]
}
```

