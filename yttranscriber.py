#!/usr/bin/env python3
"""
yttranscriber.py: Download audio from a YouTube link and transcribe it to text using Whisper.
"""
import argparse
import os
import yt_dlp
import whisper


def download_audio(youtube_url):
    # Use a persistent cache directory in the current working directory
    cache_dir = os.path.join(os.getcwd(), "audio_cache")
    os.makedirs(cache_dir, exist_ok=True)

    # Get video info (without download) to extract video ID
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        video_id = info["id"]

    cached_audio_path = os.path.join(cache_dir, f"{video_id}.mp3")
    if os.path.exists(cached_audio_path):
        return cached_audio_path, video_id

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(cache_dir, f"{video_id}.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        audio_path = (
            os.path.splitext(os.path.join(cache_dir, f'{video_id}.{info["ext"]}'))[0]
            + ".mp3"
        )
        return audio_path, video_id


def transcribe_audio(audio_path, model_name="base", language="en"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, language=language)
    return result["text"]


def format_text(text, width=80):
    import textwrap

    return "\n".join(textwrap.wrap(text, width=width))


def main():
    parser = argparse.ArgumentParser(description="YouTube Audio Transcriber")
    parser.add_argument("--url", required=True, help="YouTube video URL")
    parser.add_argument("--output", help="Output text file path")
    args = parser.parse_args()

    print("Downloading audio...")
    audio_path, video_id = download_audio(args.url)
    print("Transcribing audio...")
    text = transcribe_audio(audio_path)
    formatted_text = format_text(text)

    output_path = args.output or f"{video_id}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    print(f"Transcription saved to {output_path}")


if __name__ == "__main__":
    main()
