from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

api = YouTubeTranscriptApi()

def extract_transcript(youtube_video_url):
    try:
        # Extract video ID from URL
        if "v=" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1]
            video_id = video_id.split("&")[0]
        elif "youtu.be/" in youtube_video_url:
            video_id = youtube_video_url.split("youtu.be/")[1]
            video_id = video_id.split("?")[0]
        else:
            raise ValueError("Invalid YouTube URL")

        # Call .fetch() on the API instance
        transcript_list = api.fetch(video_id)

        transcript = " ".join([entry.text for entry in transcript_list])

        return transcript

    except VideoUnavailable:
        return "Error: Video is unavailable."
    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "Error: No transcript found for this video."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    print("Welcome to the YouTube Video Transcript Extractor!")
    youtube_link = input("Enter the URL of the video: ")

    transcript = extract_transcript(youtube_link)
    print("\nHere is the transcript of the YouTube video:\n")
    print(transcript)