from tkinter.filedialog import asksaveasfile
from pytube import YouTube
from tkinter import *

def mp4():
    final_url = link.get()
    yt = YouTube(final_url).streams.filter(progressive=True, file_extension='mp4')
    yt.order_by('resolution').desc().first().download()
    f = asksaveasfile(initialfile=yt, mode='w', defaultextension=".mp4")

def mp3():
    final_url = link.get()
    yt = YouTube(final_url).streams.filter(only_audio=True).order_by('abr').desc().first().download()
    f = asksaveasfile(initialfile=yt, mode='w', defaultextension=".mp3")

root = Tk()
root.title("Youtube Downloader")
linkLabel = Label(root, text="Entrez le lien : ")
link = StringVar()
linkEntry = Entry(root, textvariable=link, width=100)
sub_btn = Button(root, text='MP4', command=mp4)
sub_btn2 = Button(root, text='MP3', command=mp3)
# if link.get() != "":
#     url = link.get()
#     videoTitle = YouTube(url).title
#     videoCover = YouTube(url).thumbnail_url
#     response = requests.get(videoCover)
#     img = Image.open(BytesIO(response.content))
#     videoTitle = Label(root, text=videoTitle)

root.geometry("800x600")
linkLabel.pack(pady=10, side=TOP)
linkEntry.pack()
sub_btn.pack(pady=15)
sub_btn2.pack(pady=15)
# videoTitle.pack(pady=17)
# img.thumbnail((200, 200), Image.ANTIALIAS)

root.mainloop()
