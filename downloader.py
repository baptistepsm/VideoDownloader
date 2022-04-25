from tkinter.filedialog import asksaveasfile
from pytube import YouTube
from tkinter import *

def submit():
    final_url = link.get()
    print(final_url)
    f = asksaveasfile(mode='w', defaultextension="*.*")

root = Tk()
root.title("Youtube Downloader")
linkLabel = Label(root, text="Enter the link : ")
link = StringVar()
linkEntry = Entry(root, textvariable=link, width=100)
sub_btn = Button(root, text='Submit', command=submit)
root.geometry("800x600")
linkLabel.pack(pady=10, side=TOP)
linkEntry.pack()
sub_btn.pack(pady=15)

root.mainloop()
