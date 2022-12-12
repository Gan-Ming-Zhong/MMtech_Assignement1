from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo
import datetime

window= Tk()
window.title("Video Player")
window.geometry("500x500")
window.configure(bg="orange")

frame=Frame(window)
frame.pack(fill="both",side=BOTTOM)

lbl1= Label(window, text="Video Player", bg="red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)

videoplayer= TkinterVideo(master=window, scaled=True)



def openFile():
    file=askopenfile(mode="r",filetypes=[('Video Files', ["*.mp4"])])
    
    if file is not None:
        global filename
        filename= file.name
        global videoplayer
        #videoplayer= TkinterVideo(master=window, scaled=True)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

def playFile():
    videoplayer.play()

def stopFile():
    videoplayer.stop()
        
def pauseFile():
    videoplayer.pause()

def seek(value):
    videoplayer.seek(int(value))

def skip(value:int):
    videoplayer.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get()+value)

def update_duration(event):
    duration = videoplayer.video_info()["duration"]

    end_time["text"] = str(datetime.timedelta(seconds = duration))
    progress_slider["to"]=duration

def update_scale(event):
    progress_value.set(videoplayer.current_duration())

def video_ended(event):
    progress_slider.set(progress_slider["to"])
    #play_pause_btn["text"] = "Play"
    progress_slider.set(0)

image_icon = PhotoImage(file="icon\logo.png")
window.iconphoto(False,image_icon)
 
openbutton= Button(window, text="OPEN",command=lambda:openFile())
openbutton.pack(side=BOTTOM,pady=2)

playbutton= Button(window, text="PLAY",command=lambda:playFile())
playbutton.pack(side=BOTTOM,pady=3)

stopbutton= Button(window, text="STOP",command=lambda:stopFile())
stopbutton.pack(side=BOTTOM,pady=4)

pausebutton= Button(window, text="PAUSE",command=lambda:pauseFile())
pausebutton.pack(side=BOTTOM,pady=5)

Buttonbackward = PhotoImage(file = "icon\\backward.png")
back_Button=Button(frame,image = Buttonbackward, bd = 0,height = 50, width = 50, command=lambda:skip(-5),bg="orange").pack(side=LEFT)

Buttonforward = PhotoImage(file = "icon\\forward.png")
forward_Button = Button(frame,image =Buttonforward, bd = 0, height = 50, width = 50, command=lambda:skip(5),bg="orange").pack(side=RIGHT)

progress_value = IntVar(window)

progress_slider = Scale(frame,variable = progress_value,from_=0,to =0, orient = "horizontal", command=seek)
progress_slider.pack(side = "bottom", fill="x",expand= True)


videoplayer.bind("<<Duration>>",update_duration)
videoplayer.bind("<<SecondChanged>>", update_scale)

videoplayer.bind("<<Ended>>",video_ended)



start_time = Label(window, text = str(datetime.timedelta(seconds = 0)),bg="#FFFFFF")
start_time.pack(side="bottom")

end_time = Label(window,text = str(datetime.timedelta(seconds=0)))
end_time.pack(side = "bottom")



lbl1.pack()

window.mainloop()
