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

