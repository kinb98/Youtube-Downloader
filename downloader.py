
from pytube import YouTube 
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

font = ('verdana',20)
file_size = 0

def downloader(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return 
    
    try:
        yt = YouTube(url)
        st = yt.streams.first()
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)
        file_size = st.filesize
        st.download(output_path = path_to_save)
        showinfo("Message","File has been downloaded")
    except Exception as e:
        print(e)

def btnClicked():
    try:
        btn['text'] = "Downloading..."
        btn['state'] = 'disabled'
        url = urlField.get()
        if url == "":
            return 
        thread = Thread(target=downloader,args=(url,))
        thread.start()

    except Exception as e:
        print(e)

#video completion function
def completeDownload(stream=None,file_path=None):
    print("Download completed")
    showinfo("Message","File has been downloaded")
    btn['text'] = "Download video"
    btn['status'] = "active"
    urlField.delete(0,END)


# on progress 
def progressDownload(streamNone,chunk=None,bytes_remaining=None):
    percent = ((file_size-bytes_remaining)/file_size) * 100
    btn['text'] = "{:00.0f}% downloaded".format(percent)

# GUI
root = Tk()
root.title("Youtube downloader")
#root.iconbitmap("img/icon.ico")
root.geometry("500x600")

#icon
file =  PhotoImage(file="img/youtube.png")
headingIcon = Label(root,image=file)
headingIcon.pack(side=TOP,pady=3)

#url field
urlField = Entry(root,font=font,justify = CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
urlField.focus()

#download button
btn = Button(root,text="Download",font=font,relief='ridge',command=btnClicked)
btn.pack(side=TOP,pady=20)


root.mainloop()