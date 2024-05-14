from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

# Function to fetch video metadata using YouTube Data API
def fetch_video_metadata(video_url):
    # Parse the video ID from the URL
    video_id = parse_qs(urlparse(video_url).query).get('v')
    if video_id:
        video_id = video_id[0]
    else:
        print("Invalid YouTube video URL")
        return None

    # Initialize YouTube Data API client
    api_key = "AIzaSyA-Vdn3h2m9jQiu2CG-UhRtidx7i_8jWfQ"  # Replace with your own API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        # Call the videos().list method to fetch video details
        video_info = youtube.videos().list(
            part='snippet,contentDetails',
            id=video_id
        ).execute()

        # Extract relevant metadata from the response
        video_data = video_info['items'][0]
        title = video_data['snippet']['title']
        duration = video_data['contentDetails']['duration']

        # Format duration (e.g., "PT3M2S" -> "3 minutes 2 seconds")
        duration = duration.replace('PT', '').replace('H', ' hours ').replace('M', ' minutes ').replace('S', ' seconds ')

        # Get thumbnail URL
        thumbnail_url = video_data['snippet']['thumbnails']['default']['url']

        return {
            'title': title,
            'duration': duration,
            'thumbnail_url': thumbnail_url
        }
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
video_url = input("Enter the YouTube video URL: ")
metadata = fetch_video_metadata(video_url)
if metadata:
    print("Title:", metadata['title'])
    print("Duration:", metadata['duration'])
    print("Thumbnail URL:", metadata['thumbnail_url'])


# aduio extraction using ffmpeg
import subprocess
import os

# Function to extract audio from the video using FFmpeg
def extract_audio(video_url, output_dir):
    # Parse the video ID from the URL
    video_id = parse_qs(urlparse(video_url).query).get('v')
    if video_id:
        video_id = video_id[0]
    else:
        print("Invalid YouTube video URL")
        return

    # Set output file path
    output_file = os.path.join(output_dir, f"{video_id}.mp3")

    try:
        # Specify the full path to the FFmpeg executable
        ffmpeg_path = r'C:\temp\ffmpeg\bin'  # Replace with the actual path to ffmpeg.exe on your system

        # Execute FFmpeg command to extract audio
        subprocess.run([ffmpeg_path, '-i', f'https://www.youtube.com/watch?v={video_id}', '-vn', '-acodec', 'libmp3lame', '-y', output_file], check=True)
        print("Audio extracted successfully:", output_file)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
        return

# Example usage
output_directory = "Downloads"  # Replace with the desired output directory
extract_audio(video_url, output_directory)
