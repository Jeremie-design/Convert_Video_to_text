# Convert Video to Text

A Python tool that turns any video files (both local files and YouTube videos) into ASCII art. 

---

## Features

- Converts **local video files** (`.mp4`, `.avi`, `.mov`, `.mkv`, etc.)
- Converts **YouTube videos** directly from a URL
---

## Getting Started

- Python 3.8+
- `pip` (Python package manager)
- [FFmpeg](https://ffmpeg.org/download.html) 

```bash
ffmpeg -version
```

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Jeremie-design/Convert_Video_to_text.git
cd Convert_Video_to_text
```

---

## Usage

### Converts a local video file

```bash
python main.py --file path/to/your/video.mp4
```

### Convert a YouTube video to ASCII

```bash
python main.py --url https://www.youtube.com/watch?v=your_video_id
```

The converted video will be saved as a `.txt` file in the output folder.

---


##  Notes

- Long videos may take a few minutes to process.
- Internet connection required for YouTube transcription
- I am kinda bad at code so it takes a really long time to produce something
