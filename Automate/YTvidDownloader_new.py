import os
import subprocess

#without using pytube
def download_youtube_video():
    try:

        url = input("Enter the YouTube URL: ").strip()
        output_path = input("Enter the directory to save the video (leave blank for current directory): ").strip()
        if not output_path:
            output_path = os.getcwd()
        os.makedirs(output_path, exist_ok=True)

        # Use yt-dlp to download the video
        print("Downloading... Please wait.")
        subprocess.run(["yt-dlp", "-f", "best", "-o", f"{output_path}/%(title)s.%(ext)s", url])
        print(f"Download completed! Video saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()

#using ffempeg for Best Quality 
'''import os
import subprocess

def download_youtube_video():
    try:
        # Input YouTube video URL
        url = input("Enter the YouTube URL: ").strip()

        # Input destination directory
        output_path = input("Enter the directory to save the video (leave blank for current directory): ").strip()
        if not output_path:
            output_path = os.getcwd()

        # Ensure the directory exists
        os.makedirs(output_path, exist_ok=True)

        # Use yt-dlp to download the best video and audio separately, then merge
        print("Downloading... Please wait.")
        subprocess.run([
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",  # Ensures best video and audio quality
            "--merge-output-format", "mp4",  # Merges into MP4 format
            "-o", f"{output_path}/%(title)s.%(ext)s",  # Saves file with the video title
            url
        ])
        print(f"Download completed! Video saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()'''

