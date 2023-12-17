from pytube import YouTube
import tkinter 
from tkinter import filedialog

def download(url,path):
    try:
        yt=YouTube(url)  #Grab Instances from the Video
        streams=yt.streams.filter(progressive=True,file_extension='mp4')
        highest= streams.get_highest_resolution()
        highest.download(output_path=path)
        print("Video Downloaded Successfully")

    except Exception as e:
        print(e)

def opendirectory():
    folder=filedialog.askdirectory()
    if folder:   #Folder Path
        print(f"selected folder:{folder}")
    return folder

if __name__=="__main__":
    window=tkinter.Tk()    #Tkinter Window and hiding it Here(to be able to use filedialog)
    window.withdraw()
    url=input("Enter the Url of the Youtube Video : ")
    path= opendirectory()

    if not path:
        print("Please Select a Folder..")
    else:
        print("Download Started..")
        download(url,path)
