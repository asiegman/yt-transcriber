# YouTube Audio Transcriber

A simple command-line utility to download audio from a YouTube link and generate a plain text transcription using OpenAI Whisper.

## Features
- Download audio from a YouTube video
- Transcribe spoken words to text (English, local, open source)
- Output transcription as a plain text file
- Cross-platform (Linux, Windows, Mac)

## Requirements
- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (for downloading audio)
- [openai-whisper](https://github.com/openai/whisper) (for transcription)
- [ffmpeg](https://ffmpeg.org/) (required by yt-dlp and Whisper)

## Installation

1. Install Python dependencies:
   ```bash
   pip install yt-dlp openai-whisper
   ```
2. Install ffmpeg (if not already installed):
   - Linux: `sudo apt install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Windows: [Download from ffmpeg.org](https://ffmpeg.org/download.html)

## Usage

```bash
python yttranscriber.py --url <YOUTUBE_URL> [--output <output.txt>]
```

- `--url` (required): The YouTube video URL
- `--output` (optional): Output file path (default: `<video_id>.txt` in current directory)

## Example

```bash
python yttranscriber.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Notes
- Only English transcription is supported in this version.
- All processing is done locally; no data is sent to external servers.
- For best performance, a machine with a GPU is recommended, but CPU works as well (slower).

## License
MIT
