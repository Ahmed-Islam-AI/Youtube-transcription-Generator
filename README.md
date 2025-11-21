# YouTube Transcript Generator: Hybrid Approach

This project provides a comprehensive solution for extracting transcripts from YouTube videos. It utilizes a **Hybrid Strategy** to ensure high success rates regardless of whether the video creator has enabled closed captions.

## 🚀 Project Overview

There are two distinct methods implemented in this repository:

1.  **Method A (Fast):** Uses `youtube_transcript_api` to fetch existing transcripts/subtitles directly from YouTube metadata. This is instant but fails if the creator has disabled subtitles.
2.  **Method B (Robust):** Uses OpenAI's **Whisper** model to download the audio and perform AI-powered Speech-to-Text (ASR). This works on *any* video with clear audio, even if transcripts are disabled.

---

## 🛠️ Prerequisites

### System Requirements
* **Python 3.8+**
* **FFmpeg:** Required for Method B (Whisper) to process audio files.
    * *Windows:* `winget install ffmpeg`
    * *Mac:* `brew install ffmpeg`
    * *Linux:* `sudo apt install ffmpeg`
* **GPU (Optional but Recommended):** Method B runs significantly faster with an NVIDIA GPU (CUDA).

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd youtube-transcript-generator
````

2.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

-----

## 📖 Usage Guide

### Method 1: The Extractor Script (Primary Method)

*Use this first. It is lightweight and instant.*

This script attempts to pull the official or auto-generated captions provided by YouTube.

**How to run:**

```bash
python yt_transcript_extractor.py
```

1.  Paste the YouTube URL when prompted.
2.  The script will output the text to the console.

**Limitations:**

  * Will return an error if `TranscriptsDisabled` or `NoTranscriptFound`.

-----

### Method 2: Whisper AI Notebook (Fallback Method)

*Use this if Method 1 fails.*

This method uses `yt-dlp` to extract audio and OpenAI's Whisper (Medium model) to generate a fresh transcript from scratch.

**How to run:**

1.  Open `Youtube_Transcription_using_Whisper.ipynb` in Jupyter Lab or Google Colab.
2.  If using **Google Colab** (Recommended for free GPU access):
      * Upload the notebook to Drive/Colab.
      * Change Runtime type to **T4 GPU**.
3.  If running **Locally**:
      * Ensure you have FFmpeg installed.
      * Update the path variables in the notebook to point to your local directories instead of `google.colab` drive paths.

**Workflow:**

1.  **Input:** Provide the YouTube video URL.
2.  **Download:** The script extracts the audio stream using `yt-dlp`.
3.  **Transcribe:** The Whisper Model (`medium`) processes the audio.
4.  **Output:** Generates `.txt`, `.srt`, `.vtt`, and `.json` files.

-----

## ⚙️ Technical Implementation

| Feature | Method 1 (API) | Method 2 (Whisper) |
| :--- | :--- | :--- |
| **Technology** | `youtube_transcript_api` | OpenAI Whisper + PyTorch |
| **Speed** | Instant (\< 2 seconds) | Slower (depends on video length) |
| **Accuracy** | High (Official captions) | High (AI Generated) |
| **Hardware** | CPU is fine | GPU recommended |
| **Best For** | Standard videos | Videos with captions disabled |

## 📝 Notes

  * **Model Selection:** The notebook is configured to use the `medium` Whisper model. You can change this to `small` for speed or `large` for higher accuracy in the configuration cell.
  * **Legal:** Please ensure you comply with YouTube's Terms of Service regarding content usage.

<!-- end list -->
