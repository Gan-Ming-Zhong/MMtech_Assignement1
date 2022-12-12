from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo

window= Tk()
window.title("Video Player")
window.geometry("500x500")
window.configure(bg="orange")
lbl1= Label(window, text="Video Player", bg="red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)


def openFile():
    file=askopenfile(mode="r",filetypes=[('Video Files', ["*.mp4"])])
    
    if file is not None:
        global filename
        filename= file.name
        global videoplayer
        videoplayer= TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

def playFile():
    videoplayer.play()

def stopFile():
    videoplayer.stop()
        
def pauseFile():
    videoplayer.pause()
    

openbutton= Button(window, text="OPEN",command=lambda:openFile())
openbutton.pack(side=BOTTOM,pady=2)

playbutton= Button(window, text="PLAY",command=lambda:playFile())
playbutton.pack(side=BOTTOM,pady=3)

stopbutton= Button(window, text="STOP",command=lambda:stopFile())
stopbutton.pack(side=BOTTOM,pady=4)

pausebutton= Button(window, text="PAUSE",command=lambda:pauseFile())
pausebutton.pack(side=BOTTOM,pady=5)

lbl1.pack()

window.mainloop()

