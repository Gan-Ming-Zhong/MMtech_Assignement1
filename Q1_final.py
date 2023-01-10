import cv2
import os
#FrameRate
if __name__ == '__main__' :
 
    video = cv2.VideoCapture("C:\Visual Studio\.vscode\Assignment MMTech\surveillance_5.mp4");
 
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
 
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS): {0}".format(fps))

#Resolution       
    file_path = ('C:\Visual Studio\.vscode\Assignment MMTech\surveillance_5.mp4')
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    print("Resolution: {}x{}".format(width, height))

#VideoSize
    video_size = os.path.getsize('C:\Visual Studio\.vscode\Assignment MMTech\surveillance_5.mp4' )
    print("File Size: ", video_size, "bytes")

    video.release()
