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

### Use Server

```bash
curl -F "file=@examples/en.mp3" http://127.0.0.1:7860/whisper
```

