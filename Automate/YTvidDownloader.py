from pytube import YouTube
import tkinter 
from tkinter import filedialog

def download(url, path, download_type):
    try:
        yt = YouTube(url)  # Grab Instances from the Video
        if download_type == "video":
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            highest = streams.get_highest_resolution()
        elif download_type == "audio":
            streams = yt.streams.filter(only_audio=True, file_extension='mp4') #As Mp4 is used for both Audio and Video due to yt structure
            highest = streams.first()

        highest.download(output_path=path)
        print(f"{download_type.capitalize()} Downloaded Successfully")

    except Exception as e:
        print(e)

def opendirectory():
    folder = filedialog.askdirectory()
    if folder:   # Folder Path
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    window = tkinter.Tk()    # Tkinter Window and hiding it here (to be able to use filedialog)
    window.withdraw()

    url = input("Enter the URL of the YouTube video: ")
    path = opendirectory()

    if not path:
        print("Please select a folder...")
    else:
        download_type = input("Enter 'video' to download as MP4 or 'audio' to download as MP3: ").lower()
        if download_type not in ["video", "audio"]:
            print("Invalid choice. Please enter 'video' or 'audio'.")
        else:
            print(f"Download started as {download_type}...")
            download(url, path, download_type)
