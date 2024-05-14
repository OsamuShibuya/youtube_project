from pytube import YouTube
import requests
from PIL import Image
from io import BytesIO

def download_audio(video_url, output_directory):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download(output_path=output_directory)

    # Rename the downloaded file to have a .mp3 extension
    # Pytube doesn't automatically provide the file extension
    import os
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)
    print(f"Audio saved as: {new_file}")
    
    # Download thumbnail
    thumbnail_url = yt.thumbnail_url
    thumbnail_request = requests.get(thumbnail_url)
    
    # Open thumbnail image using PIL
    thumbnail_image = Image.open(BytesIO(thumbnail_request.content))
    
    # Resize the thumbnail to desired dimensions (e.g., 128x128)
    thumbnail_image = thumbnail_image.resize((1080, 1280))
    
    thumbnail_file = os.path.join(output_directory, f"{base}.jpg")
    with open(thumbnail_file, 'wb') as f:
        f.write(thumbnail_request.content)
    print(f"thumbnail saved as: {base}.jpg")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = "Downloads"
    download_audio(video_url, output_directory)